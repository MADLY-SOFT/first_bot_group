import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = 'BOT_TOKEN'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.reply("Привет! Я твой простой бот. Отправь мне команду /text.")

@dp.message()
async def handle_text_command(message: types.Message):
    response_text = "Это ответ на команду /text. Ты можешь изменить этот текст."
    await message.reply(response_text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
