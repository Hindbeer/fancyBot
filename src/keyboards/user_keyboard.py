from dataclasses import dataclass
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


@dataclass()
class UserKeyboard:
    main_buttons = [
        [
            KeyboardButton(text="главная"),
            KeyboardButton(text="корзина")
        ],
        [
            KeyboardButton(text="настройки"),
            KeyboardButton(text="профиль"),
            KeyboardButton(text="о боте")
        ]
    ]

    main_keyboard = ReplyKeyboardMarkup(keyboard=main_buttons,
                                        resize_keyboard=True,
                                        input_field_placeholder="Выберите пункт меню")