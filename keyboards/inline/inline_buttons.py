from aiogram import types


def groups():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Подобрать группу", callback_data="choose_group")
    btn2 = types.InlineKeyboardButton(text="Список групп", callback_data="groups_list")
    menu.add(btn1, btn2)

    return menu


def group_types():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Психологоия", callback_data="psycho")
    btn2 = types.InlineKeyboardButton(text="Криптовалюта", callback_data="crypto")
    btn3 = types.InlineKeyboardButton(text="Стартапы", callback_data="startup")
    menu.add(btn1, btn2, btn3)

    return menu


def yes_no():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="yes")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="no")
    menu.add(btn1, btn2)

    return menu


def back_to_menu():
    menu = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back_to_menu")
    menu.add(btn1)

    return menu  