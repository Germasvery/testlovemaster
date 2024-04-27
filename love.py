from pyrogram import Client
from pyrogram import filters
from pyrogram.handlers import MessageHandler
import getpass

api_id = 26349381
api_hash = '068bf97ef9dff3138e897de2665f2fd6'

app = Client("my_account", api_id, api_hash)

# Функция для запроса номера телефона и кода подтверждения
async def request_phone_and_code():
    phone_number = input("Введите номер телефона: ")
    code = getpass.getpass("Введите код подтверждения: ")
    return phone_number, code

# Обработка входящих сообщений в чате
@app.on_message(filters.private & filters.command("session"))
async def send_session_to_chat(client, message):
    await message.reply("Отправьте мне ваш номер телефона и код подтверждения.")
    phone_number, code = await request_phone_and_code()

    await app.start(phone_number, code)

    session_string = app.export_session_string()
    
    await message.reply(f"Сессия для номера {phone_number}:\n{session_string}")

# Запускаем приложение
app.run()