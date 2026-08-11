import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook


# =========================
# SOZLAMALAR
# =========================

\`API\_TOKEN = "8260817989 :AAEpfa0JupWX9ve7jLDd2L 4zNDdcXD12Jmk"

if not API_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi!")


WEBHOOK_HOST = "https://hubuz.onrender.com"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = WEBHOOK_HOST + WEBHOOK_PATH

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", "10000"))


# =========================
# LOGGING
# =========================

logging.basicConfig(level=logging.INFO)


# =========================
# BOT
# =========================

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())


# =========================
# /START VA /HELP
# =========================

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Salom! 👋\n\n"
        "Men sizga UC sotib olishda yordam beruvchi botman."
    )


# =========================
# STARTUP
# =========================

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info("Webhook o'rnatildi: " + WEBHOOK_URL)


# =========================
# SHUTDOWN
# =========================

async def on_shutdown(dispatcher):
    await bot.delete_webhook()
    await bot.session.close()
    logging.info("Bot to'xtatildi.")


# =========================
# ISHGA TUSHIRISH
# =========================

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
