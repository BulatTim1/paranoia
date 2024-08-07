import datetime
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

from pydantic import BaseModel, ConfigDict, StringConstraints

# Create the engine
engine = sa.create_engine(f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@db/{Config.POSTGRES_DB}")

# Create a session factory
Session = sessionmaker(bind=engine)

# Create the base class for declarative models
Base = declarative_base()


class Token(BaseModel):
    access_token: str | bytes
    token_type: str

class TokenData(BaseModel):
    user_id: int | None = None

class UserOrm(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    telegram_id = sa.Column(sa.BigInteger, nullable=True, default=None)
    guid_token = sa.Column(sa.String, nullable=True)
    fullname = sa.Column(sa.String)
    joined_at = sa.Column(sa.DateTime, default=sa.func.now())
    is_banned = sa.Column(sa.Boolean, default=False)
    points = sa.Column(sa.Integer, default=0)

    def login_user(self, user_id) -> bool:
        res = False
        with Session() as session:
            self.telegram_id = user_id
            self.guid_token = None
            try:
                session.commit()
                res = True
            except:
                session.rollback()
        return res

    @staticmethod
    def get_user_by_guid(guid_token):
        with Session() as session:
            return session.query(UserOrm).filter_by(guid_token=guid_token).first()

    @staticmethod
    def get_user_by_tg_id(telegram_id):
        with Session() as session:
            return session.query(UserOrm).filter_by(telegram_id=telegram_id).first()
    
    @staticmethod
    def get_user_by_id(user_id):
        with Session() as session:
            return session.query(UserOrm).filter_by(id=user_id).first()
    
    def to_model(self):
        return UserModel(id=self.id, telegram_id=self.telegram_id, fullname=self.fullname, 
                         joined_at=self.joined_at, is_banned=self.is_banned, points=self.points)

class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    telegram_id: int
    # guid_token: str
    fullname: str
    joined_at: datetime.datetime
    is_banned: bool
    points: int

class GameConfig(Base):
    __tablename__ = 'game_config'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    start_round = sa.Column(sa.Time, default=datetime.time(6, 0))
    round_duration = sa.Column(sa.Interval, default=datetime.timedelta(hours=15))
    identified_threshold = sa.Column(sa.Integer, default=10)
    lizards_count = sa.Column(sa.Integer, default=3)
    survey_count = sa.Column(sa.Integer, default=5)

class RoundOrm(Base):
    __tablename__ = 'round'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    issued_at = sa.Column(sa.Date, default=sa.func.now())
    winner = sa.Column(sa.Enum('rus', 'liz'), nullable=True, default=None)
    identified_threshold = sa.Column(sa.Integer, default=10)
    start_round = sa.Column(
        sa.DateTime,
        default=lambda: datetime.datetime.combine(
            datetime.date.today(), datetime.time(6, 0)
        ),
    )  # utc
    round_duration = sa.Column(sa.Interval, default=datetime.timedelta(hours=15))
    lizards_count = sa.Column(sa.Integer, default=3)
    survey_count = sa.Column(sa.Integer, default=5)

    def to_model(self):
        return RoundModel(id=self.id, issued_at=self.issued_at, winner=self.winner, 
                          identified_threshold=self.identified_threshold, start_round=self.start_round, 
                          round_duration=self.round_duration, lizards_count=self.lizards_count, 
                          survey_count=self.survey_count)

    @property
    def is_over(self):
        return datetime.now() > self.start_round + self.round_duration

    @staticmethod
    def most_recent():
        round = None
        with Session() as session:
            round = session.query(RoundOrm).order_by(RoundOrm.issued_at.desc()).one()
        return round

    @staticmethod
    def currently_running():
        round = RoundOrm.most_recent()
        if round.is_over:
            round = None
        return round


class RoundModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    issued_at: datetime.date
    winner: str
    identified_threshold: int
    start_round: datetime.time
    round_duration: datetime.timedelta
    lizards_count: int
    survey_count: int


class RoundDataModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    start_round: datetime.datetime
    round_duration: datetime.timedelta
    is_over: bool
    lizards_count: int
    is_lizard: bool
    winner: str


class TaskOrm(Base):
    __tablename__ = 'task'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
    is_fake = sa.Column(sa.Boolean, default=False)

class TaskModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    is_active: bool
    is_fake: bool

class LizardOrm(Base):
    __tablename__ = 'lizard'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    task_id = sa.Column(sa.Integer, sa.ForeignKey('task.id'), nullable=True, default=None) # TODO: review this

    @property
    def task(self):
        task = None
        with Session() as session:
            task = session.query(TaskOrm).filter_by(id=self.task_id).one()
        return task


class LizardModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    round_id: int
    task_id: int

class GuessOrm(Base):
    __tablename__ = 'guess'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    guessed_user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    is_correct = sa.Column(sa.Boolean, nullable=True, default=None)

class GuessModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    round_id: int
    guessed_user_id: int

class GuessPostModel(BaseModel):
    guessed_user_id: int

class SurveyTaskOrm(Base):
    __tablename__ = 'survey'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    task_id = sa.Column(sa.Integer, sa.ForeignKey('task.id'))
    answer = sa.Column(sa.Boolean, nullable=True, default=None)
    
    def to_model(self):
        return SurveyTaskModel(id=self.id, user_id=self.user_id, 
                               round_id=self.round_id, task_id=self.task_id, 
                               answer=self.answer)

class SurveyTaskModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    round_id: int
    task_id: int
    answer: bool | None

class SurveyPostModel(BaseModel):
    task_id: int
    answer: bool

# Create or update the tables
Base.metadata.create_all(bind=engine, checkfirst=True)

# TODO: integrate alembic for migrations
