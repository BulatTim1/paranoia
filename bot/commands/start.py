import logging
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram import types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from states.login import Guid
from globals import dp, User

def user_auth(user_id):
    user = User.get_user_by_tg_id(user_id)
    return True if user else False

form_router = Router()

@form_router.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    logging.info(message)
    if user_auth(message.from_user.id):
        wa = WebAppInfo(url='https://paranoia.bulattim.ru/')
        ikb = InlineKeyboardButton(text="Меню", web_app=wa)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[[ikb]])

        await message.reply("Привет! Ты успешно авторизован!", reply_markup=keyboard)
        # await state.update_data(guid=Guid.guid)
        await state.finish()
    else:
        await message.reply("Введите токен!")
        await state.update_data(guid=Guid.guid)

@form_router.message(Guid.guid)
async def add_category(message: Message, state: FSMContext):
    logging.info(message)
    user_id = message.from_user.id
    user = User.get_user_by_guid(message.text.strip())
    if user:
        res = user.init_user(user_id)
        if res:
            await message.reply("Авторизация успешна")
            wa = WebAppInfo(url='https://paranoia.bulattim.ru/')
            ikb = InlineKeyboardButton(text="Меню", web_app=wa)
            keyboard = InlineKeyboardMarkup()
            keyboard.add(ikb)
    await message.reply("Неверный токен")
