import logging
import sys
from aiogram import executor as ex
from commands import start
from globals import dp


async def bot_callback(x):
    print("Started")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    ex.start_polling(dp, on_startup=bot_callback, skip_updates=True)
