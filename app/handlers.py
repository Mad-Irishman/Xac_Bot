from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from app.keyboards import button_profile, button_create_list, button_create_appeal, button_feedback

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    if True:
        await message.answer(f'Вы авторизированы',
                             reply_markup=await button_profile())


@router.message(F.text == 'Мой профиль ⚙️')
async def create_list(message: Message):
    await message.answer(text=f'Выберите 👇', reply_markup=await button_create_list())


@router.callback_query(F.data == 'Создать обращение')
async def create_appeal_repair(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Создать обращение 📝', reply_markup=await button_create_appeal())


@router.callback_query(F.data == 'Обратная связь')
async def feedback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Обратная связь 🗣', reply_markup=await button_feedback())

