import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """Handler for /start command"""
    # Create inline keyboard with WebApp button
    web_app_url = os.getenv("WEBAPP_URL")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити Mini App", web_app=WebAppInfo(url=web_app_url))]
    ])
    
    await message.answer("Ласкаво просимо! Натисніть кнопку нижче, щоб відкрити Mini App:", reply_markup=keyboard)

async def main() -> None:
    """Main function to start the bot"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())