from aiogram import types
import requests as requests

from aiogram.types import InlineKeyboardButton

from bot_app.app import contacts_response

contacts_menu_inline = types.InlineKeyboardMarkup(row_width=1)
contacts_list = [{"text": "🌎 Наш сайт Oksana-Veld.ru", "url": "https://oksana-veld.ru/"}]
for contact in contacts_response:
    if 'Телефон' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"☎️ {contact['contact_name']}: {contact['value']}",
                                 callback_data=contact['contact_name']))
    elif 'E-mail' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"💌 {contact['contact_name']}: {contact['value']}",
                                 callback_data=contact['contact_name']))
    elif 'Адрес' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"📍 {contact['contact_name']}: {contact['value']}", url=contact['link'],
                                 callback_data=contact['contact_name']))
    elif 'Instagram' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"🤳🏻 {contact['contact_name']}: {contact['value']}", url=contact['link'],
                                 callback_data=contact['contact_name']))
    elif 'Telegram' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"💬 {contact['contact_name']}: {contact['value']}", url=contact['link'],
                                 callback_data=contact['contact_name']))
    elif 'VKontakte' in contact['contact_name']:
        contacts_list.append(
            InlineKeyboardButton(text=f"👩🏼‍💻 {contact['contact_name']}: {contact['value']}", url=contact['link'],
                                 callback_data=contact['contact_name']))
    else:
        contacts_list.append(
            InlineKeyboardButton(text=f"{contact['contact_name']}: {contact['value']}", url=contact['link'],
                                 callback_data=contact['contact_name']))
print(contacts_list)
contacts_menu_inline.add(*contacts_list)
