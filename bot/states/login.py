from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from globals import User, dp


class Guid(StatesGroup):
    guid = State()

@dp.message_handler(state=Guid.guid)
async def add_category(message: types.Message, state: FSMContext):
    logging.info(message)
    user_id = message.from_user.id
    user = User.get_user_by_guid(message.text.strip())
    if user:
        res = user.init_user(user_id)
        if res:
            await message.reply("Авторизация успешна")
    await message.reply("Неверный токен")
    await state.finish()
