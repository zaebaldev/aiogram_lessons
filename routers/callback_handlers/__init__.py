from aiogram import Router, F, types

# from aiogram.types.callback_query import CallbackQuery
from .info import router as callback_data_router

router = Router()
router.include_routers(callback_data_router)
