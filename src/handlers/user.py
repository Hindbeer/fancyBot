from aiogram.types import Message

from src.main import bot, dp

from src.keyboards import UserKeyboard


@dp.message_handler(commands='start')
async def start(message: Message):
    await bot.send_message(message.chat.id, '''
🥴 Привет, я помогу тебе оформить заказ! 
Нажми на кнопки ниже, или введи нужную тебе команду! (/help)

❗ Этот бот является тестовым полигоном, вы ничего не сможете тут купить! 

''', reply_markup=UserKeyboard.main_keyboard)


@dp.message_handler(commands='help')
async def helping(message: Message):
    await bot.send_message(message.chat.id, '''
Все команды бота: 
    
🔍 /help - Список всех команд
👥 /profile - Ваш профиль 
🏪 /shop - Главная страница магазина
🗂 /cart - Корзина товаров
🎙 /about - Описание проекта
⚙ /settings - Настройки
    
Данные команды аналогичны пунктам меню, которые появляются на клавиатуре.
    
    ''')


@dp.message_handler(text="главная")
async def show_catalog(message: Message):
    await bot.send_message(message.chat.id, "Выберите раздел, чтобы вывести список товаров:")
