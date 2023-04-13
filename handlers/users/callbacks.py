from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import inline_buttons
from utils.misc.group_links import links

# ---------Первый этап. инлайн кнопки: (Подобрать группу, Список групп)---------

# Подобрать группу
@dp.callback_query_handler(text_contains='choose_group', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer("Чем вы интересуетесь?", reply_markup=inline_buttons.group_types())

# Список групп
@dp.callback_query_handler(text_contains='groups_list', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    text = "\n".join([[k + ' - ' + ', '.join(v)][0] for k, v in links.items()])  # Здесь мы преобразуем текст нужный нам образом 
    await c.message.answer(text, disable_web_page_preview=True)
# ------------------


# ---------Второй этап. инлайн кнопки: (Психологоия, Криптовалюта, Стартапы)---------


@dp.callback_query_handler(lambda c: c.data.startswith('theme_'), state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    # Здесь сохроняем тематику группы, чтобы позже его определять
    async with state.proxy() as data:
        data['type'] = c.data[6:]

    if c.data[6:] == 'Психология':
        await c.message.edit_text("Вы психолог?", reply_markup=inline_buttons.yes_no())

    elif c.data[6:] == 'Криптовалюта':
        await c.message.edit_text("Вы торгуете криптовалютой?", reply_markup=inline_buttons.yes_no())

    elif c.data[6:] == 'Стартапы':
        await c.message.edit_text("Вы создаете стартап?", reply_markup=inline_buttons.yes_no())
    
    else:
        await c.message.edit_text("Вы работаете на этой сфере?", reply_markup=inline_buttons.yes_no())
# ------------------


# ---------Третий этап. инлайн кнопки: (Да, Нет)---------


@dp.callback_query_handler(text_contains='yes', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        group_type = data.get("type")

    text = ", ".join(links[group_type])
    await c.message.edit_text(text, reply_markup=inline_buttons.back_to_menu())


@dp.callback_query_handler(text_contains='no', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        group_type = data.get("type")

    text = ", ".join(links[group_type])
    await c.message.edit_text(text, reply_markup=inline_buttons.back_to_menu())
# ------------------


# ---------Четвертый этап. инлайн кнопки: (Вернуться в меню)---------


@dp.callback_query_handler(text_contains='back_to_menu', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.message.edit_text("Главное меню", reply_markup=inline_buttons.groups())
# ------------------
