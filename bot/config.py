import json
import os


class Config:
    """Configurations for the bot"""
    TG_TOKEN = os.environ.get('TG_TOKEN', '')
    TG_BOT = os.environ.get('TG_BOT', '')
    TG_ADMIN = json.loads(os.environ.get('TG_ADMINS', '[]'))
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')