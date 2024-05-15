import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message 
from aiogram.filters.command import Command 

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

rus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 
        'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 
        'Ч', 'Ш', 'Щ', 'Ы', 'Ъ', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 
        'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',          'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы',            
        'ъ', 'э', 'ю', 'я']
eng = ['A', 'B', 'V', 'G', 'D', 'E', 'E', 'ZH', 'Z', 'I', 'I', 'K', 
        'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'KH', 'TS',
        'CH', 'SH', 'SHCH', 'Y', 'IE', 'E', 'IU', 'IA', 'a', 'b', 'v', 
        'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 
        'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 
        'shch', 'y', 'ie', 'e', 'iu', 'ia']


@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введи ФИО на русском языке, а я верну его на латинице!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def translit_name(message: Message):
    namee = message.text
    translit_name = ''.join([eng[rus.index(i)] if i in rus else i for i in namee])
    logging.info(f'{user_name} {user_id}: {name}')
    await message.reply(translit_name)

# Определяем процесс пуллинга (просим диспетчер(Dispatcher) обращаться к серверам Телеграмма на наличие обновлений)
if __name__ == '__main__':
    dp.run_polling(bot)