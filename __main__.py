from loop import loop
from bot import dp
from aiogram import executor


if __name__ == "__main__":
    loop.create_task()
    executor.start_polling(dp, loop=loop, skip_updates=True)
