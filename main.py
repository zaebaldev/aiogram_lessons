import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import settings
from routers import router
from db import cursor
from aiogram.filters import Command

bot = Bot(token=str(settings.api_token))
dp = Dispatcher()


@dp.message(Command("users"))
async def get_all_users(message: Message):
    users = cursor.execute("SELECT * FROM users")
    fetched_users = users.fetchall()
    print(fetched_users)
    for user in fetched_users:
        await message.answer(
            text=user[1],
        )


async def main():
    print("I start polling")
    dp.include_router(router)
    await dp.start_polling(bot)
    cursor.close()
    print("Cursor closed")


if __name__ == "__main__":
    asyncio.run(main())
