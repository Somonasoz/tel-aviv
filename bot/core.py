import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from os import environ as env
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = env.get('TOKEN')
URL_GET_PHONE = env.get('URL_GET_PHONE')
GROUP_ID = env.get('GROUP_ID')

# Configure logging

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)