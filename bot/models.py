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
    
    def login_user(self, telegram_id) -> bool:
        res = False
        with Session() as session:
            self.telegram_id = telegram_id
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
        
    @staticmethod
    def get_user_by_id(user_id):
        with Session() as session:
            return session.query(User).filter_by(id=user_id).first()
    
    @staticmethod
    def add_user(telegram_id, fullname):
        with Session() as session:
            user = User(telegram_id=telegram_id, fullname=fullname)
            session.add(user)
            session.commit()
            return user
