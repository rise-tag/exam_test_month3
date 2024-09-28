from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from db import add_client_data
from keyboards import client_keyboard
from generate_code import generate_personal_code

class ClientForm(StatesGroup):
    name = State()
    surname = State()
    phone = State()

async def start(message: types.Message):
    await message.answer("Добро пожаловать! Введите ваше имя")
    await ClientForm.name.set()

async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Теперь введите ваше полное фамилия")
    await ClientForm.surname.set()

async def process_surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Введите ваш номер телефона")
    await ClientForm.phone.set()

async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    user_data = await state.get_data()

    personal_code = generate_personal_code()
    add_client_data(user_data['name'], user_data['surname'], user_data['phone'], personal_code)

    await message.answer(f"Ваш персональный код: {personal_code}\nАдрес склада в Китае: Шанхай, ул. Чжэньин, д. 7.", reply_markup=client_keyboard())
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state="*")
    dp.register_message_handler(process_name, state=ClientForm.name)
    dp.register_message_handler(process_surname, state=ClientForm.surname)
    dp.register_message_handler(process_phone, state=ClientForm.phone)
import sqlite3

def add_client_data(name, surname, phone, personal_code):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (name, surname, phone, personal_code) VALUES (?, ?, ?, ?)', (name, surname, phone, personal_code))
    conn.commit()
    conn.close()
