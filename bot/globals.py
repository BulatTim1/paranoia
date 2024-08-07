import logging, sys
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import Config
from models import User, Session

storage = MemoryStorage()
bot = Bot(token=Config.TG_TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
