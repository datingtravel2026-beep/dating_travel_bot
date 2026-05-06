from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Профиль"), KeyboardButton(text="Поиск")],
            [KeyboardButton(text="Анонимка"), KeyboardButton(text="Магазин")],
            [KeyboardButton(text="О нас")]
        ],
        resize_keyboard=True
    )
