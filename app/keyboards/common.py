from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def subscription_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Канал",
                    url="https://t.me/your_channel"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 Чат",
                    url="https://t.me/your_chat"
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
