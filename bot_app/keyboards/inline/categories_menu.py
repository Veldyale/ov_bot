from aiogram import types
from aiogram.types import InlineKeyboardButton

from bot_app.app import categories_response
from bot_app.keyboards.inline.callback_datas import category_callback

categories_inline = types.InlineKeyboardMarkup(row_width=1)
category_item = []

for category in categories_response:
    category_item.append(
        InlineKeyboardButton(text=f'{category["category_name"]} 🔽', callback_data=category_callback.new(category_name=category["category_name"], id=category["id"])))
categories_inline.add(*category_item)