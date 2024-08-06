import json
import os

class Config:
    """Configurations for the bot"""
    TG_TOKEN = os.environ.get('TG_TOKEN', '')
    TG_BOT = os.environ.get('TG_BOT', '')
    TG_ADMIN = json.loads(os.environ.get('TG_ADMINS', '[]'))
    JWT_TOKEN = os.environ.get('JWT_TOKEN', 'secret-dasfdsfsdmfsd')

    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'test')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'test')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'test')
