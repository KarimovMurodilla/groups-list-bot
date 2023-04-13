from aiogram import types

from utils.misc.group_links import links


def groups(): # кнопки для меню
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Подобрать группу", callback_data="choose_group")
    btn2 = types.InlineKeyboardButton(text="Список групп", callback_data="groups_list")
    menu.add(btn1, btn2)

    return menu


def group_types(): # кнопки для выбора тематики группы
    menu = types.InlineKeyboardMarkup(row_width=1)

    for name in links.keys():
        btn = types.InlineKeyboardButton(text=name, callback_data=f"theme_{name}")
        menu.add(btn)

    return menu


def yes_no(): # кнопки для выбора Да или Нет
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="yes")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="no")
    menu.add(btn1, btn2)

    return menu


def back_to_menu(): # Возврат в меню
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back_to_menu")
    menu.add(btn1)

    return menu  