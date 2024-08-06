import datetime
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

# Create the engine
engine = sa.create_engine(f"postgresql://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@db/{Config.POSTGRES_DB}")

# Create a session factory
Session = sessionmaker(bind=engine)

# Create the base class for declarative models
Base = declarative_base()


# Define your models
class User(Base):
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
            return session.query(User).filter_by(guid_token=guid_token).first()

    @staticmethod
    def get_user_by_tg_id(telegram_id):
        with Session() as session:
            return session.query(User).filter_by(telegram_id=telegram_id).first()

class GameConfig(Base):
    __tablename__ = 'game_config'
    start_round = sa.Column(sa.Time, default=datetime.time(9, 0, tzinfo=datetime.timezone.utcoffset(3)))
    round_duration = sa.Column(sa.Interval, default=datetime.timedelta(hours=15))
    survey_threshold = sa.Column(sa.Integer, default=10, min=0, max=100)

class Round(Base):
    __tablename__ = 'round'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    issued_at = sa.Column(sa.Date, default=sa.func.now())
    winner = sa.Column(sa.Enum('rus', 'liz'), nullable=True, default=None)
    identified_threshold = sa.Column(sa.Integer, default=10, min=0, max=100)
    start_round = sa.Column(sa.Time, default=datetime.time(9, 0, tzinfo=datetime.timezone.utcoffset(3)))
    round_duration = sa.Column(sa.Interval, default=datetime.timedelta(hours=15))

class Task(Base):
    __tablename__ = 'task'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
    is_fake = sa.Column(sa.Boolean, default=False)

class Lizard(Base):
    __tablename__ = 'lizard'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    task_id = sa.Column(sa.Integer, sa.ForeignKey('task.id'), nullable=True, default=None) # TODO: review this

class Guess(Base):
    __tablename__ = 'guess'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    guessed_user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))

class SurveyTask(Base):
    __tablename__ = 'survey'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    round_id = sa.Column(sa.Integer, sa.ForeignKey('round.id'))
    task_id = sa.Column(sa.Integer, sa.ForeignKey('task.id'))
    answer = sa.Column(sa.Boolean, nullable=True, default=None)

# Create or update the tables
Base.metadata.create_all(bind=engine, checkfirst=True)
