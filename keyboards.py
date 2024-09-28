from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def client_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_template = KeyboardButton("Получить шаблон заполнения")
    keyboard.add(button_template)
    return keyboard
