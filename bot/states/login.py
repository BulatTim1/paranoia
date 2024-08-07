from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from globals import User, dp


class Guid(StatesGroup):
    guid = State()
