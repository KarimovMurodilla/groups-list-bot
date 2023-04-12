from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class CallbackQueryMiddleware(BaseMiddleware):
    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        await callback_query.answer()
