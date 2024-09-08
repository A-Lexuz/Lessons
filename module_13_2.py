import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token='botToken')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def bot_react1(message):
    print('Введите команду /start, чтобы начать общение')
    await message.answer('Введите команду /start, чтобы начать общение')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())