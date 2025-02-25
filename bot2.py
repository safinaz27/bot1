import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()  # تحميل المتغيرات من ملف .env

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply(f"اهلا يا لوزر")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
