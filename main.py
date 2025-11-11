import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, user
from config import settings
from routers import router
from db import cursor
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State

bot = Bot(token=str(settings.api_token))
dp = Dispatcher()


class Users(StatesGroup):
    user_id = State()


@dp.message(Command("users"))
async def get_all_users(message: Message):
    try:
        users = cursor.execute("SELECT * FROM users")
        fetched_users = users.fetchall()
        print(fetched_users)
        for user in fetched_users:
            await message.answer(
                text=user[1],
            )
    except Exception:
        await message.answer("Something went wrong!")


@dp.message(Command("user_by_id"))
async def get_user_by_id(message: Message, state: FSMContext):
    await state.set_state(Users.user_id)
    await message.answer("Enter user ID")


@dp.message(Users.user_id)
async def handle_user_form_name(message: Message, state: FSMContext):
    if message.text:
        try:
            user_id = int(message.text)
            users = cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
            fetched_user = users.fetchone()
            print(fetched_user)
            await message.answer(
                f"Username: {fetched_user[1]} Email: {fetched_user[2]}"
            )
            await state.clear()
        except ValueError:
            await message.answer("Please, correct ID")


@dp.message(Command("db_clear"))
async def clear_all_data(message: Message):
    tables = ["staff", "users"]
    for table in tables:
        cursor.execute(f"DROP TABLE {table}")
    await message.answer("all tables successfully deleted")


async def main():
    print("I start polling")
    dp.include_router(router)
    await dp.start_polling(bot)
    cursor.close()
    print("Cursor closed")


if __name__ == "__main__":
    asyncio.run(main())
