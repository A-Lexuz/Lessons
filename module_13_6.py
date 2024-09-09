from aiogram import Bot, Dispatcher, types, Router, F
import asyncio
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton,
                           InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

router = Router()
bot = Bot(token='token')
dp = Dispatcher()

def inline_keyboard(): #пробуем создавать клавиатуры через InlineKeyboardMarkup (нововведение 3.х версии Aiogram)
    ikbuttons = [
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
         InlineKeyboardButton(text='Формула расчёта', callback_data='formula')]]
    return InlineKeyboardMarkup(inline_keyboard=ikbuttons, resize_keyboard=True)
def keyboard_start():   #пробуем создавать клавиатуры через ReplyKeyboardBuilder (нововведение 3.х версии Aiogram)
    kb = ReplyKeyboardBuilder()
    button_info = KeyboardButton(text = 'Информация')
    button_calories = KeyboardButton(text = 'Рассчитать калории')
    kb.add(button_calories, button_info)
    return kb.as_markup(resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    print(f'{message.chat.first_name} {message.chat.last_name} запустил бота')
    await message.answer("Привет! Я бот, помогающий твоему здоровью. "
                         "Вы можете попросить просчитать вашу ежедневную норму калорий.",
                         reply_markup=keyboard_start())

@dp.message(F.text == "Информация")
async def bot_react(message: types.Message, state: FSMContext):
    await message.answer(f'Данный бот имеет функционал простого расчёта ежедневной нормы калорий, '
                         f'и разработан в качестве домашнего задания к урокам Urban University')
    await state.set_state(UserState.age)

@dp.message(F.text == "Рассчитать калории")
async def bot_react(message: types.Message, state: FSMContext):
    await message.answer(text='Желаете расчитать норму калорий или хотите увидеть формулы Миффлина-Сан Жеора?',
                         reply_markup=inline_keyboard())

@dp.callback_query(F.data == 'formula')
async def get_formula(call):
    await call.message.answer('Простейшие формулы по Миффлину - Сан Жеору:\n'
                              'Женская формула: 10 х вес + 6,25 х рост – 5 х возраст – 161.\n'
                              'Мужская формула: 10 х вес + 6,25 х рост – 5 х года + 5',
                              reply_markup=ReplyKeyboardRemove())
    await call.answer()

@dp.callback_query(F.data == 'calories')
async def bot_react(call: types.Message, state: FSMContext):
    await call.message.answer(f'Давайте начнём. Введите свой возраст:', reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.age)
    await call.answer()

@dp.message(UserState.age)
async def bot_react_2(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer(f'А теперь напишите свой рост:')
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def bot_react_3(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer(f'А теперь мне нужен Ваш вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def bot_react_4(message: types.Message, state: FSMContext):
    await state.update_data(weigh=int(message.text))
    await message.answer(f"Хорошо, осталось лишь указать ваш пол",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Мужской"),KeyboardButton(text="Женский"),]], resize_keyboard=True,),)
    await state.set_state(UserState.gender)

@dp.message(UserState.gender, F.text == 'Мужской')
async def bot_react_final(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    await message.answer(f'{message.chat.first_name} {message.chat.last_name}, Ваша норма калорий: '
                         f'{10 * data['weigh'] + 6.25 * data['growth'] - 5 * data['age'] + 5}',
                         reply_markup=ReplyKeyboardRemove(),)
    await state.clear()

@dp.message(UserState.gender, F.text == 'Женский')
async def bot_react_final(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    await message.answer(f'{message.chat.first_name}, Ваша норма калорий: '
                         f'{10 * data['weigh'] + 6.25 * data['growth'] - 5 * data['age'] - 161}',
                         reply_markup=ReplyKeyboardRemove(),)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())