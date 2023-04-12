from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from keyboards.inline import inline_buttons


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    user = message.from_user
    db_user = await db.get_user(user.id)

    if not db_user:
        await db.reg_user(user.id, user.username, user.first_name)

    await message.answer("Привет! Я бот, который поможет тебе выбрать группу по твоим интересам", 
        reply_markup=inline_buttons.groups())