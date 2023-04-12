from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.inline import inline_buttons
from keyboards.default import keyboard_buttons


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    
    await message.answer("Привет! Я вот, который позволит тебе узнать чуть больше обо мне", 
        reply_markup=None)