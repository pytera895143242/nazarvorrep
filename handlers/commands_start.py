from aiogram import types
from misc import dp, bot
from .sqlit import reg_user
from aiogram.dispatcher import FSMContext

content =  -1001977186979

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    if len(message.text) == 6:
        reg_user(message.chat.id, 'SprintArbitraj')  # Регистрация в БД
    else:
        reg_user(message.chat.id, message.text[7:])  # Регистрация в БД

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Погнали🔥', callback_data='go_1')
    markup.add(bat_a)
    await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=20,reply_markup=markup)
