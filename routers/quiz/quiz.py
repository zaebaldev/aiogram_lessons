from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from db import cursor, connection

router = Router()


class UserForm(StatesGroup):
    username = State()
    email = State()


@router.message(Command("quiz", prefix="/!"))
async def handle_quiz_commanf(message: types.Message, state: FSMContext):
    await state.set_state(UserForm.username)
    await message.answer(
        text="Hi there! Whats your username?",
    )


@router.message(UserForm.username)
async def handle_user_form_name(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(UserForm.email)
    await message.answer(
        text="Enter ur email, now",
    )


@router.message(UserForm.email)
async def handle_user_form_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    user_data = await state.get_data()
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (user_data.get("username"), user_data.get("email")),
    )
    connection.commit()
    await state.clear()
    await message.answer(text="Your data successfully created!")
