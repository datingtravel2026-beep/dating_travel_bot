from aiogram import Router, types
from aiogram.filters import CommandStart

from app.database.queries import get_user, create_user
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    user = await get_user(message.from_user.id)

    if not user:
        await create_user(message.from_user.id)

    await message.answer(
        "Добро пожаловать в Dating Travel 🌍\nНажми кнопку ниже чтобы начать"
    )
