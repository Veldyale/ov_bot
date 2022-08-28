from aiogram import types
import requests as requests

from aiogram.types import InlineKeyboardButton

from bot_app.app import services_response
from bot_app.keyboards.inline import callback_datas


services_inline = types.InlineKeyboardMarkup(row_width=1)
service_item = []

# services_menu_inline = types.InlineKeyboardMarkup(row_width=1)
# service_list = []
# print(callback_datas.category_callback, 'callback')
# for service in services_response:
#     if int(service['category']) == int(callback_datas.category_callback):
#     # if int(service['category']) == 1:
#         service_list.append(InlineKeyboardButton(text=service['service_name'], callback_data=service['id']))
# services_menu_inline.add(*service_list)
#
# await call.message.answer(text='Вы перешли в услуги', reply_markup=services_menu_inline)
# await call.message.delete()
