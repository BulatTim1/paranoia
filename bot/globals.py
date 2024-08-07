from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config
from models import User, Session

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
