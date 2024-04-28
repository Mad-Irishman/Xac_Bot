from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def builder_create_list():
    array = ['Создать обращение', 'Обратная связь']
    keyboard = InlineKeyboardBuilder()
    for l in array:
        keyboard.add(InlineKeyboardButton(text=l, callback_data=l))
    return keyboard.adjust(1).as_markup()


def builder_create_appeal():
    array_topic = ['Жалобы', 'Запросы на ремонт', 'Предложения']
    topic = InlineKeyboardBuilder()
    for t in array_topic:
        topic.add(InlineKeyboardButton(text=t, callback_data=t))
    return topic.adjust(2).as_markup()


def builder_create_feedback_statictiks():
    array_statictiks = [str(x) for x in range(1, 6)]
    feedback_statictiks = InlineKeyboardBuilder()
    for s in array_statictiks:
        feedback_statictiks.add(InlineKeyboardButton(text=s, callback_data=s))
    return feedback_statictiks.adjust(5).as_markup()

