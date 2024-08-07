import logging
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from states.login import Guid
from globals import dp, User


def user_auth(user_id):
    user = User.get_user_by_tg_id(user_id)
    return True if user else False


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    logging.info(message)
    await state.finish()
    if user_auth(message.from_user.id):
        ikb = InlineKeyboardButton("Перейти", web_app=WebAppInfo(url='https://paranoia.bulattim.ru/'))

        keyboard = InlineKeyboardMarkup()
        keyboard.add(ikb)

        await message.reply("Привет! Ты успешно авторизован!", reply_markup=keyboard)
    else:
        await message.reply("Введите токен!")
        await state.update_data(guid=Guid.guid)
