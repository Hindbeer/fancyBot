from aiogram.types import Message

from src.main import bot, dp


@dp.message_handler(commands='start')
async def start(message: Message):
    await bot.send_message(message.chat.id, 'Привет, я ботик абармотик!')
