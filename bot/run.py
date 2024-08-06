from aiogram import executor as ex

from globals import dp


async def bot_callback(x):
    print("Started")


if __name__ == '__main__':
    ex.start_polling(dp, on_startup=bot_callback)
