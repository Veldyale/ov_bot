from aiogram import types

from bot_app.app import dp, bot
from bot_app.keyboards.reply.main_menu import markup_start
from bot_app.messages import WELCOME_MESSAGE


@dp.message_handler(commands=['start'])  # команда /start
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, WELCOME_MESSAGE,
                           reply_markup=markup_start)
    await message.delete()