import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from routers import router

bot = Bot(token=str(settings.api_token))
dp = Dispatcher()


async def main():
    print("I start polling")
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

print("some changes")
