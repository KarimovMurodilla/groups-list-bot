from aiogram import types


def groups_list():
    menu = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="", callback_data="")
    menu.add(btn1)

    return menu