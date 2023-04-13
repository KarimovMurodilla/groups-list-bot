from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from .broadcast import broadcaster
from states.input_message import InputMessage
from keyboards.inline import admin_inline_buttons

from utils.misc.xlsx.export import export_to_xlsx


@dp.callback_query_handler(text_contains="unload_users", state="*")
async def unload_users(c: types.CallbackQuery, state: FSMContext):
    msg = await c.message.answer("Выгружаем пользователей")
    await export_to_xlsx() # экспортируем данные из базы данных в xlsx файл 
    await msg.delete()
    await c.message.answer_document(types.InputFile('users.xlsx')) # отправляем готовый файл


@dp.callback_query_handler(text_contains="send_to_users", state="*")
async def send_to_users(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer("Введите сообщение")
    await InputMessage.get_message.set()


@dp.message_handler(state=InputMessage.get_message)
async def process_get_message(message: types.Message):
    count = await broadcaster(message.text) # рассылка сообщения, и в то же время возвращает количество отправленных сообщений
    await message.answer(f"Отправлено {count} пользователям", reply_markup=admin_inline_buttons.admin_panel())
