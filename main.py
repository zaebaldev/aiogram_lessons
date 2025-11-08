import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import settings
from routers import router
from db import cursor, connection

bot = Bot(token=str(settings.api_token))
dp = Dispatcher()


@dp.message()
async def handle_user_name(message: Message):
    full_name = message.from_user.full_name
    await message.answer(text=f"username is {full_name}")
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (full_name, f"{full_name}@email.com"),
    )
    connection.commit()


async def main():
    print("I start polling")
    dp.include_router(router)
    await dp.start_polling(bot)
    cursor.close()
    print("Cursor closed")


if __name__ == "__main__":
    asyncio.run(main())
