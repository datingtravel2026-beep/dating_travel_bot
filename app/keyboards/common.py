from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def subscription_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Канал",
                    url="https://t.me/DatingTravel"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 Чат",
                    url="https://t.me/DatingTravelChat"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Проверить",
                    callback_data="check_sub"
                )
            ]
        ]
    )
