from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_services = KeyboardButton('Прайс-лист 📃️')
# button_services = KeyboardButton('Услуги ✂️')
button_mode = KeyboardButton('Расписание ✅')
# button_your_mode = KeyboardButton('Ваши записи 📆', request_location=True)
button_contacts = KeyboardButton('Контакты 📇️')
markup_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_start.add(button_services, button_mode, button_contacts, )