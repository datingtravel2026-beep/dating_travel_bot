from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def gender_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мужчина"), KeyboardButton(text="Девушка")],
            [KeyboardButton(text="Пара"), KeyboardButton(text="Би")]
        ],
        resize_keyboard=True
    )


def confirm_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Подтвердить")],
            [KeyboardButton(text="Редактировать")]
        ],
        resize_keyboard=True
    )
