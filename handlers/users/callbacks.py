from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import inline_buttons
from utils.misc.group_links import links

# ------------------


@dp.callback_query_handler(text_contains='choose_group', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer("Чем вы интересуетесь?", reply_markup=inline_buttons.group_types())


@dp.callback_query_handler(text_contains='groups_list', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):

    text = "\n".join([l[0] for l in links.values()])
    await c.message.answer(text, disable_web_page_preview=True)
# ------------------


# ------------------


@dp.callback_query_handler(text_contains='psycho', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = c.data
    await c.message.edit_text("Вы психолог?", reply_markup=inline_buttons.yes_no())


@dp.callback_query_handler(text_contains='crypto', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = c.data
    await c.message.edit_text("Вы торгуете криптовалютой?", reply_markup=inline_buttons.yes_no())


@dp.callback_query_handler(text_contains='startup', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = c.data
    await c.message.edit_text("Вы создаете стартап?", reply_markup=inline_buttons.yes_no())
# ------------------


# ------------------


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


# ------------------


@dp.callback_query_handler(text_contains='back_to_menu', state="*")
async def cancel_handler(c: types.CallbackQuery, state: FSMContext):
    await c.message.edit_text("Главное меню", reply_markup=inline_buttons.groups())
# ------------------