from aiogram import Bot, Dispatcher, types, Router, F
import asyncio
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton,
                           InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from crud_functions import *

router = Router()
bot = Bot(token='7148520650:AAHJr1cxNLwVmPT0VoMMoRJ1ZWszku9XC9k')
dp = Dispatcher()

tablets = ('https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66042077276cdf0c037197e7_660420eb74b4ea5e8752bfd7/scale_1200',
           'https://otvet.imgsmail.ru/download/22d3da69736dd70184a931a2fe8576e0_i-5993.jpg',
           'https://cs9.pikabu.ru/post_img/2017/08/26/8/og_og_1503755906213651319.jpg',
           'https://i.pinimg.com/736x/74/95/60/7495605acfc07d03a7dbbeeb7f14b67c.jpg')

initiate_db()

def inline_keyboard(): #пробуем создавать клавиатуры через InlineKeyboardMarkup (нововведение 3.х версии Aiogram)
    ikbuttons = [
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
         InlineKeyboardButton(text='Формула расчёта', callback_data='formula')]]
    return InlineKeyboardMarkup(inline_keyboard=ikbuttons, resize_keyboard=True)

def inline_keyboard_buy():
    ikbuttons = [
        [InlineKeyboardButton(text='Фуфломицин', callback_data='fuf'),
         InlineKeyboardButton(text='Балбесин', callback_data='balb'),
         InlineKeyboardButton(text='Пофигин', callback_data='pof'),
         InlineKeyboardButton(text='Что-нибудь от головы', callback_data='golov')]]
    return InlineKeyboardMarkup(inline_keyboard=ikbuttons, resize_keyboard=True)

def keyboard_start():   #пробуем создавать клавиатуры через ReplyKeyboardBuilder (нововведение 3.х версии Aiogram)
    kb = ReplyKeyboardBuilder()
    button_info = KeyboardButton(text='Информация')
    button_calories = KeyboardButton(text='Рассчитать калории')
    button_buy = KeyboardButton(text='Купить')
    button_register = KeyboardButton(text='Регистрация')
    kb.add(button_calories, button_info, button_buy,button_register)
    return kb.as_markup(resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    username = State()
    email = State()
    userage = State()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    print(f'{message.chat.first_name} {message.chat.last_name} запустил бота')
    await message.answer("Привет! Я бот, помогающий твоему здоровью. "
                         "Вы можете попросить просчитать вашу ежедневную норму калорий.",
                         reply_markup=keyboard_start())

@dp.message(F.text == "Информация")
async def bot_react(message: types.Message):
    await message.answer(f'Данный бот имеет функционал простого расчёта ежедневной нормы калорий, покупке лекарств '
                         f'и разработан в качестве домашнего задания к урокам Urban University')


@dp.message(F.text == "Купить")
async def get_buying_list(message):
    products = get_all_products()
    for i in range (4):
        await message.answer_photo(tablets[i], f'Продукт {products[i][0]} | Описание: {products[i][1]}  '
                                          f'| Цена: {products[i][2]}')
    await message.answer('Какой продукт желаете купить?',reply_markup=inline_keyboard_buy())




@dp.message(F.text == 'Регистрация')
async def sign_up(message: types.Message, state: FSMContext):
    await message.answer(f'Введите имя пользователя (только латинский алфавит):',
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserState.username)


@dp.message(UserState.username)
async def set_username(message: types.Message, state: FSMContext):
    if check_user(message.text) != None:
        await message.answer(f'Пользователь уже существует, введите другое имя:')
        await state.set_state(UserState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer(f'Введите Ваш e-mail:')
        await state.set_state(UserState.email)

@dp.message(UserState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(f'Введите Ваш возраст:')
    await state.set_state(UserState.userage)

@dp.message(UserState.userage)
async def set_age(message: types.Message, state: FSMContext):
    try:
        int(message.text)
    except:
        await message.answer('Неверно указан возраст, попробуйте еще раз:')
        await state.set_state(UserState.userage)

    await state.update_data(userage=int(message.text))
    await message.answer('Регистрация успешно завершена!')
    new_user = await state.get_data()
    add_user(new_user['username'],new_user['email'],new_user['userage'])
    await state.clear()



@dp.callback_query(F.data == 'fuf')
async def accept_buy (call):
    await call.message.answer('Спасибо за покупку! "Фуфломицин", лекарство от всего, даже от короновируса!',
                              reply_markup=ReplyKeyboardRemove())

@dp.callback_query(F.data == 'balb')
async def accept_buy (call):
    await call.message.answer('Спасибо за покупку! "Балбесин", лекарство поможет для Вашего ума... можеть быть!',
                              reply_markup=ReplyKeyboardRemove())
@dp.callback_query(F.data == 'pof')
async def accept_buy (call):
    await call.message.answer('Спасибо за покупку! "Пофигин", берегите Ваши нервы!',
                              reply_markup=ReplyKeyboardRemove())
@dp.callback_query(F.data == 'golov')
async def accept_buy (call):
    await call.message.answer('Нужно чего-нибудь от головы, но топора под рукой нет? Наше лекарство "Что-нибудь от'
                              'головы поможет вам! Спасибо за покупку!',
                              reply_markup=ReplyKeyboardRemove())

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
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())