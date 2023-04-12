from aiogram.dispatcher.filters.state import State, StatesGroup


class InputMessage(StatesGroup):
    get_message = State()
