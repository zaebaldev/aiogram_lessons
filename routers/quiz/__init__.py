from aiogram import Router
from .quiz import router as quiz_fsm_router

router = Router()

router.include_routers(quiz_fsm_router)
