from random import randint
from aiogram import types, Bot, Dispatcher,executor
import logging
from PIL import Image
from loaddata import catordog
logging.basicConfig(level=logging.INFO)
bot = Bot(token='5077133016:AAFeAjz4GDOe_39siIkaenFULthrEQ07YLY')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def echo(message: types.Message):
   await message.answer('Привет! Я бот с ИИ умеющий отличать кошек от собак. Скинь фотку, что бы в этом убедиться')


@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    filname='images/'+str(randint(1,100))+'.jpg'
    await message.photo[-1].download(destination_file=filname)
    img = Image.open(filname)
    answer=catordog(img)
    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)