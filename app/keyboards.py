from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.builder import builder_create_list, builder_create_appeal, builder_create_feedback_statictiks


async def button_profile():
    my_profil = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Мой профиль ⚙️')]
    ], resize_keyboard=True)
    return my_profil


async def button_create_list():
    return builder_create_list()


async def button_create_appeal():
    return builder_create_appeal()


async def button_feedback():
    return builder_create_feedback_statictiks()
