from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
import json
import logging
from typing import Annotated
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

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 1

app = FastAPI(servers=[{"url": "https://paranoia.bulattim.ru/api/"}])
security = APIKeyCookie(name="access_token")
logger = logging.getLogger("uvicorn")

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
            auth_date = int(item[10:-1])
        sorted_data.append(item)
    if data_hash == "" or auth_date == -1:
        return False
    secret_key = hmac.new('WebAppData'.encode(), Config.TELEGRAM_BOT_TOKEN.encode(), hashlib.sha256).digest()
    hash = hmac.new(secret_key, "&".join(sorted_data).encode(), hashlib.sha256).hexdigest()
    return hash == data_hash and auth_date > datetime.now().timestamp() - Config.TOKEN_EXPIRE_IN_SECONDS

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


async def get_current_lizard(
    current_user: Annotated[UserOrm, Depends(get_current_user)],
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
) -> LizardOrm:
    lizard = None
    with Session() as session:
        lizard = (
            session.query(LizardOrm)
            .filter_by(user_id=current_user.id, round_id=current_round.id)
            .one()
        )
    if lizard is None:
        raise HTTPException(status_code=400, detail="Not a current lizard")
    return lizard


@app.get('/token-validate')
async def validate(token: str = Depends(security)) -> dict:
    token = unquote(token)
    return json.loads(token[token.find('{'):token.find('},') + 1]) if validate_telegram_data(token) else None

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
async def get_round() -> RoundModel:
    """Get current round data."""
    round = RoundOrm.most_recent()
    if not round:
        raise HTTPException(status_code=404, detail="Round not found")
    return round.to_model()


@app.post("/guess")
async def guess(
    model: GuessPostModel,
    current_round: Annotated[RoundOrm, Depends(get_current_round)],
    current_user: Annotated[UserOrm, Depends(get_current_user)],
) -> bool:
    """Make a guess."""
    with Session() as session:
        if model.guess == current_round.winner:
            current_user.points += 1
            session.commit()
            return True
        return False


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
            traceback.print_exc()
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


# @app.get("/tasks")
# async def get_tasks(
#     model: SurveyPostModel,
#     current_round: Annotated[RoundOrm, Depends(get_current_round)],
#     current_user: Annotated[UserOrm, Depends(get_current_user)],
#     current_lizard: Annotated[LizardOrm, Depends(get_current_lizard)],
# ) -> SurveyTaskModel | None:
#     with Session() as session:
