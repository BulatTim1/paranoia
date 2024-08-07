# from aiogram import executor as ex
# from commands import start
import logging
import sys

from globals import dp, Config, bot
from aiogram.client.session.middlewares.request_logging import RequestLogging
from aiogram.methods import GetUpdates
import asyncio

# async def bot_callback(x):
#     print("Started")

async def main()->None:
    bot.session.middleware(RequestLogging(ignore_methods=[GetUpdates]))
    await dp.start_polling(allowed_updates=["message"])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
