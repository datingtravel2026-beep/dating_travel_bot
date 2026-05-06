from aiogram import Router, types
from aiogram.types import CallbackQuery

from app.services.subscription import check_sub

router = Router()


@router.callback_query(lambda c: c.data == "check_sub")
async def check_subscription(callback: CallbackQuery):
    is_sub = await check_sub(callback.bot, callback.from_user.id)

    if not is_sub:
        await callback.answer("❌ Ты не подписан", show_alert=True)
        return

    await callback.message.answer(
        "✅ Подписка подтверждена!\nНажми «Начать»",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text="Начать")]],
            resize_keyboard=True
        )
    )

    await callback.answer()
