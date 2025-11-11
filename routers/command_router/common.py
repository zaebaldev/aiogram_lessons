from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from keyboards import get_request_keyboard, get_info_keyboard


router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text="Hi! I am test bot!")


@router.message(Command("help", prefix="/!"))
async def handle_help(message: types.Message):
    await message.answer(
        text="Help message",
        reply_markup=get_request_keyboard(),
    )


@router.message(Command("info"))
async def handle_info(message: types.Message):
    await message.answer(
        text="Info message",
        reply_markup=get_info_keyboard(),
    )
