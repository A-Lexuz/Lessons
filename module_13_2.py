import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token='token')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print(f'{message.chat.first_name} {message.chat.last_name} запустил бота')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def bot_react1(message):
    print(f'{message.chat.first_name} {message.chat.last_name} отправил неверную команду ({message.text})')
    await message.answer('Введите команду /start, чтобы начать общение')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())