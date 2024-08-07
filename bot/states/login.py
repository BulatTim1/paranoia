import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, WebAppInfo)
from aiogram.utils import executor
from aiogram.utils.markdown import hbold
from globals import User, bot, dp


class Guid(StatesGroup):
    guid = State()

@dp.message_handler(state=Guid.guid)
async def add_category(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = User.get_user_by_guid(message.text.strip())
    print(message.text.strip())
    if user:
        res = user.init_user(user_id)
        if res:
            await message.reply("Авторизация успешна")
    await message.reply("Неверный токен")
    await state.finish()
