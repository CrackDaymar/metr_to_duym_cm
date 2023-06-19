import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


from main import last_func


class Conversion(StatesGroup):
    waiting_for_unit = State()
    waiting_for_value = State()


bot = Bot(token='5784283337:AAF7DKFRlwI5sojiX9Gp1ollDYuIvQe770c')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logger.add('debug.log', format="{time} {level} {message}",
           level='DEBUG', rotation="10KB", compression='zip')


# Start
@logger.catch()
@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text='Сантиметры'),
        KeyboardButton(text='Миллиметры')
    )
    await message.answer('Выберите единицы измерения:', reply_markup=keyboard)


# Conversion to inches: waiting for unit
@logger.catch(level="CRITICAL")
@dp.message_handler(Text(equals=['Сантиметры', 'Миллиметры']), state=None)
async def choose_unit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['unit'] = message.text

    await Conversion.waiting_for_value.set()
    await message.answer('Введите значение:', reply_markup=types.ReplyKeyboardRemove())


# Conversion to inches: waiting for value
@logger.catch(level="CRITICAL")
@dp.message_handler(state=Conversion.waiting_for_value)
async def process_value(message: types.Message, state: FSMContext):
    try:
        value = message.text
        async with state.proxy() as data:
            unit = data['unit']

        result = ''
        if unit == 'Сантиметры':
            result = last_func(value, True)
        elif unit == 'Миллиметры':
            result = last_func(value, False)

        logger.info(f"Данные = {result}"
                    f"\n Умный пользователь = {message.chat.first_name} {message.chat.last_name}")
        await message.answer(result)
    except Exception as ex:
        await message.answer('Вы ввели не правильное значнеие, введите значение в формате "Число-Число" или же '
                             'просто единичное число')
        logger.info(f"Ошибка = {ex}"
                    f"\n Глупый пользователь = {message.chat.first_name} {message.chat.last_name}")


async def after_start(message: types.Message):
    pass


@logger.catch(level="info")
def main():
    logger.info('Start')
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
