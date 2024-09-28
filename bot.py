import sqlite3

def create_db():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        phone TEXT NOT NULL,
        personal_code TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

import random

def generate_personal_code():
    number = random.randint(100, 999)
    return f'KRE-{number}'
 
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
from handlers import register_handlers
from db import create_db

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    create_db()

if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, on_startup=on_startup)
    from aiogram import Bot, Dispatcher, types
    
from aiogram.utils import executor
from config import TOKEN
from handlers import register_handlers
from db import create_db

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    create_db()

if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, on_startup=on_startup)
