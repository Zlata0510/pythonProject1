import asyncio  # Работа с асинхронностью
from typing import Text

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет!")


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Чем могу помочь?')

#@dp.message(F.content_type == ContentType.PHOTO)
#async def echo_photo(message: Message):
#   await message.answer_photo(message.photo[0].file_id)

# @dp.message(F.content_type == ContentType.STICKER)
# async def echo_sticker(message: Message):
#     await message.answer_sticker(message.sticker.file_id)
#
# @dp.message(F.content_type == ContentType.VOICE)
# async def echo_voice(message: Message):
#     await message.answer_voice(message.voice.file_id)
@dp.message(Text(text='Ответь'))
async def reply (message:Message):
    await message.answer.reply('Ответил')

async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
