from aiogram import types
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery

from bot_app.app import dp
from bot_app.keyboards.inline.categories_menu import categories_inline
from bot_app.keyboards.inline.contacts_menu import contacts_menu_inline
from bot_app.keyboards.inline.services_menu import services_response


@dp.message_handler(content_types=['text'])  # обработчик кнопок главного меню
async def keyboard_start_action(message: Message):
    # if message.text == 'Услуги ✂️':
    if message.text == 'Прайс-лист 📃️':
        await message.answer('Вы перешли в каталог услуг', reply_markup=categories_inline)
        await message.delete()

    elif message.text == 'Расписание ✅':
        await message.answer('❕ Сейчас мы работаем только по предварительной записи\n\n✍🏻️ Пожалуйста запишитесь:\n\n☎️ по телефону\n💬 в мессенджерах\n👩🏼‍💻 в VKontakte\n🤳🏻 в Instagram\n\n🙏🏻 Благодарим Вас за понимание')
        await message.delete()

    elif message.text == 'Контакты 📇️':
        await message.answer('🔎 Наши контакты:', reply_markup=contacts_menu_inline)
        await message.delete()

    else:
        await message.answer('🤖 Данный информационный бот не отвечает на Ваши сообщения\n\n🙏🏻 Пожалуйста воспользуйтесь меню')
        await message.delete()


@dp.callback_query_handler(lambda call: call.data)  # обработчик кнопок меню категории
async def services(call: CallbackQuery):
    if 'category' in call.data.split(':')[0]:
        category_name = str(f"🗒 {call.data.split(':')[1]}:\n\n")
        for service in services_response:
            if service['category'] == int(call.data.split(':')[2]):
                category_name = category_name + str(f"{service['service_name']} \n👉🏻 {service['prefix']} {int(service['price'])} ₽ \n\n")
        await call.message.answer(text=f'{category_name}\nℹ️ Описание услуг, 📸Фото работ и 💥Акции, Вы можете посмотреть на нашем сайте:\n\n🌐 Oksana-Veld.ru\n\n❕️Цены действительны на момент публикации')
        await call.message.delete()
