import aiogram
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from aiogram.utils import executor
from aiogram.utils.markdown import hbold
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from states.login import Guid
from globals import bot, dp


def user_auth(user_id):
    user = User.query.filter_by(telegram_id=user_id).first()
    return True if user else False


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    if user_auth(message.from_user.id):
        ikb = InlineKeyboardButton("Перейти", web_app=WebAppInfo(url='https://google.com'))

        keyboard = InlineKeyboardMarkup()
        keyboard.add(ikb)

        await message.reply("Привет! Ты успешно авторизован!", reply_markup=keyboard)
    else:
        await message.reply("Введите токен!")
        await state.update_data(guid=Guid.guid)
