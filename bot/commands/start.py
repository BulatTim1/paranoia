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

wa = WebAppInfo(url='https://paranoia.bulattim.ru/')
ikb = InlineKeyboardButton(text="Меню", web_app=wa)
keyboard = InlineKeyboardMarkup(inline_keyboard=[[ikb]])

@form_router.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    if user_auth(message.from_user.id):
        await message.reply("Привет! Ты уже авторизован!", reply_markup=keyboard)
    else:
        await message.reply("Привет, введи токен!")
        await state.set_state(Guid.guid)

@form_router.message(Guid.guid)
async def add_category(message: Message, state: FSMContext):
    logging.info(message)
    user_id = message.from_user.id
    # user = User.get_user_by_guid(message.text.strip())
    if user:
        user.login_user(user_id)
        await message.reply("Авторизация успешна", reply_markup=keyboard)
    elif user_auth(user_id):
        await message.reply("Ты уже авторизован :3", reply_markup=keyboard)
    else:
        user = User.add_user(user_id, message.text.strip()) # TODO: delete this after presentation
        await message.reply("Добро пожаловать в игру!", reply_markup=keyboard)
