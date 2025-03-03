#start bo
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

#токен бота
API_TOKEN ="7399928399:AAGVW6kBllbTUDSjfA4uPW1GI1qF2EXraM0"


#экземпляр бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


#Обработчик команды /start
@dp.message (Command(commands=["start"]))
async def process_start_command(message: types.Message):
    await nessage.answer ("HELLO!")


#Обработчик текстовых сообщений
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)
if  __name__ == "__main__":
    asyncio.run(main)