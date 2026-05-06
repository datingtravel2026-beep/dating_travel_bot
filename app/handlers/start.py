from aiogram import Router, types
from aiogram.filters import CommandStart

from app.database.queries import get_user, create_user
from app.keyboards.common import subscription_kb
from app.services.subscription import check_sub

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    user = await get_user(message.from_user.id)

    if not user:
        await create_user(message.from_user.id)

    text = (
        "🌍 Добро пожаловать в Dating Travel\n\n"
        "Здесь ты найдёшь знакомства и попутчиков ✈️"
    )

    is_sub = await check_sub(message.bot, message.from_user.id)

    if not is_sub:
        await message.answer(
            text + "\n\n❗ Подпишись на канал и чат",
            reply_markup=subscription_kb()
        )
        return

    await message.answer(
        text + "\n\nНажми «Начать», чтобы создать анкету",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text="Начать")]],
            resize_keyboard=True
        )
    )
