import logging
from .app import dp
from .keyboards.reply import main_menu
from .handlers import start_command, menus

logging.basicConfig(level=logging.INFO)