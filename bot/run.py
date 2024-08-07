# from aiogram import executor as ex
# from commands import start
from globals import dp, bot
import asyncio

# async def bot_callback(x):
#     print("Started")

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot, skip_updates=True))
