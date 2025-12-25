import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
API_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Этот обработчик будет вызываться при получении команды /start.
    """
    await message.reply("Привет! Я твой простой Telegram бот. Отправь мне любое сообщение, и я его повторю.")

# Обработчик команды /text
@dp.message_handler(commands=['text'])
async def echo_text_command(message: types.Message):
    """
    Этот обработчик будет вызываться при получении команды /text.
    """
    await message.reply("Ты отправил команду /text. Теперь отправь мне любое сообщение, и я его повторю.")

# Обработчик для всех остальных текстовых сообщений (эхо)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_all(message: types.Message):
    """
    Этот обработчик будет повторять все текстовые сообщения, которые не являются командами.
    """
    await message.reply(message.text)

if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
