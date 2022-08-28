import os

import requests
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

load_dotenv()

bot = Bot(token=os.getenv('TOKEN_BOT'))
dp = Dispatcher(bot)

categories_response = requests.get(os.getenv('CATEGORIES_URL')).json()
services_response = requests.get(os.getenv('SERVICES_URL')).json()
contacts_response = requests.get(os.getenv('CONTACTS_URL')).json()
# times_response = requests.get(os.getenv('TIMES_URL')).json()
