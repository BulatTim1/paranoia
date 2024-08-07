from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
import json
import logging
from typing import Annotated, Optional
import os
import hmac
import hashlib
from urllib.parse import unquote
from models import *
from config import Config
from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.security import APIKeyCookie
import jwt
from jwt.exceptions import InvalidTokenError
import traceback

app = FastAPI(servers=[{"url": "/api"},{"url": "https://paranoia.bulattim.ru/api/"}], root_path='/api')

security = APIKeyCookie(name="access_token")
logger = logging.getLogger("uvicorn")
secret_key = hmac.new('WebAppData'.encode(), Config.TG_TOKEN.encode(), hashlib.sha256).digest()

async def validate_telegram_data(data: str) -> bool:
    # data_check_string = ...
    # secret_key = HMAC_SHA256(<bot_token>, "WebAppData")
    # if (hex(HMAC_SHA256(data_check_string, secret_key)) == hash) {
    # // data is from Telegram
    # }
    unquoted_data = unquote(data)
    array = unquoted_data.split("&")
    sorted_data = []
    data_hash = ""
    auth_date = -1
    for item in sorted(array):
        if item.startswith("hash="):
            data_hash = item[5:]
            continue
        if item.startswith("auth_date="):
            auth_date = int(item[10:])
        sorted_data.append(item)
    if data_hash == "" or auth_date == -1:
        return False
    gen_hash = hmac.new(secret_key, "\n".join(sorted_data).encode(), hashlib.sha256).hexdigest()
    return gen_hash == data_hash and auth_date > datetime.now().timestamp() - Config.TOKEN_EXPIRE_IN_SECONDS

async def get_current_user(token: Annotated[str, Depends(security)]) -> UserOrm:
    """Get current user from TMA token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"Set-Cookie": "access_token=; Path=/; HttpOnly; Max-Age=0"} # TODO: review this
    )
    res = False
    telegram_id = None
    try:
        data = json.loads(token)
        res = validate_telegram_data(token)
    except:
        raise credentials_exception
    logger.info(res)
    if not res:
        raise credentials_exception
    telegram_id = data.get("id")
    user = UserOrm.get_user_by_tg_id(telegram_id)
    if user is None:
        raise credentials_exception
    return user

async def get_current_round() -> RoundOrm:
    round = RoundOrm.currently_running()
    if round is None:
        raise HTTPException(status_code=404, detail="No current round")
    return round

async def maybe_get_current_lizard(
    current_user: Annotated[UserOrm, Depends(get_current_user)],
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
) -> Optional[LizardOrm]:
    lizard = None
    with Session() as session:
        lizard = (
            session.query(LizardOrm)
            .filter_by(user_id=current_user.id, round_id=current_round.id)
            .one()
        )
    return lizard


async def get_current_guesses(
    current_user: Annotated[UserOrm, Depends(get_current_user)],
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
    current_lizard: Annotated[Optional[LizardOrm], Depends(maybe_get_current_lizard)],
) -> list[GuessOrm]:
    if current_lizard is not None:
        raise HTTPException(status_code=400, detail="Lizards can't guess")
    with Session() as session:
        return (
            session.query(GuessOrm)
            .filter_by(user_id=current_user.id, round_id=current_round.id)
            .all()
        )


@app.get('/token-validate')
async def validate(token: str = Depends(security)) -> dict:
    token = unquote(unquote(token))
    return json.loads(token[token.find('{'):token.find('}&') + 1]) if validate_telegram_data(token) else None

# messaging functions
@app.get("/self")
async def get_player(current_user: Annotated[UserOrm, Depends(get_current_user)]) -> UserModel:
    """Get user data."""
    return current_user.to_model()

@app.get("/players")
async def get_players(current_user: Annotated[UserOrm, Depends(get_current_user)]) -> list[UserModel]:
    """Get all users."""
    with Session() as session:
        users = session.query(UserOrm).all()
        return [user.to_model() for user in users]

@app.get("/leaderboards")
async def get_leaderboards() -> list[UserModel]:
    """Get leaderboards."""
    with Session() as session:
        users = session.query(UserOrm).order_by(UserOrm.points.desc()).limit(100).all()
        return [user.to_model() for user in users]


@app.get("/round")
async def get_round_data(
    current_user: Annotated[UserOrm, Depends(get_current_user)],
    recent_round: Annotated[Optional[RoundOrm], Depends(RoundOrm.most_recent)],
    current_lizard: Annotated[Optional[LizardOrm], Depends(maybe_get_current_lizard)],
) -> RoundModel:
    """Get current round data."""
    if recent_round is None:
        raise HTTPException(status_code=404, detail="No recent round")
    return RoundDataModel(
        start_round=recent_round.start_round,
        round_duration=recent_round.round_duration,
        is_over=recent_round.is_over,
        lizards_count=recent_round.lizards_count,
        is_lizard=(current_lizard is not None),
        winner=recent_round.winner,
    )


@app.post("/guess")
async def guess(
    model: GuessPostModel,
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
    current_user: Annotated[UserOrm, Depends(get_current_user)],
    current_guesses: Annotated[list[GuessOrm], Depends(get_current_guesses)],
) -> bool:
    """Make a guess."""
    if len(current_guesses) >= current_round.lizards_count:
        raise HTTPException(status_code=400, detail="Out of guesses")
    guessed_user = UserOrm.get_user_by_id(model.guessed_user_id)
    guessed_lizard = maybe_get_current_lizard(guessed_user, current_round)
    is_correct = guessed_lizard is not None
    guess = GuessOrm(
        user_id=current_user.id,
        guessed_user_id=guessed_user.id,
        round_id=current_round.id,
        is_correct=is_correct,
    )
    with Session() as session:
        session.add(guess)
    if is_correct:
        current_user.points += 1
    return is_correct


@app.post("/survey")
async def vote(
    model: SurveyPostModel,
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
    current_user: Annotated[UserOrm, Depends(get_current_user)],
) -> SurveyTaskModel | None:
    with Session() as session:
        try:
            survey = session.query(SurveyOrm).filter_by(user_id=current_user.id, round_id=current_round.id)
            survey.answer = model.answer
            session.commit()
        except:
            session.rollback()
            logger.error(traceback.format_exc())
        surveys = session.query(SurveyOrm).filter_by(round_id=current_round.id, user_id=current_user.id).all()
        if len(surveys) <= current_round.survey_count:
            new_survey = None
            try:
                tasks = session.query(TaskOrm).filter_by(round_id=current_round.id, is_active=True).all()
                new_survey = SurveyOrm(user_id=current_user.id, round_id=current_round.id, 
                                       task_id=random.choice(filter(lambda x: x.id not in 
                                                                    [survey.task_id for survey in surveys], 
                                                                    tasks)).id)
                session.add(new_survey)
                session.commit()
            except:
                session.rollback()
                traceback.print_exc()
            if new_survey is not None:
                return new_survey.to_model()
        return None


@app.get("/tasks")
async def get_tasks(
    current_lizard: Annotated[Optional[LizardOrm], Depends(maybe_get_current_lizard)],
) -> TaskModel | None:
    if current_lizard is None:
        return None
    else:
        return current_lizard.task.to_model()
