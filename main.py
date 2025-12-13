from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

BOT_TOKEN="8279116831:AAFxv-nlkwg5KauuEkbo5IalAuYLlWhbksM"

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

@dp.message(Command("start"))
async def handle_start(message: Message):
    await message.answer("Hello! Welcome to the bot.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())        