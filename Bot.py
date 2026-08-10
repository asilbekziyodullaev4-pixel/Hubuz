import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware 
from aiogram.utils.executor import start_webhook
APL_TOKEN= 8260817989:AAFvm8-VBVDY o1KZdmjTliCc3c5dAFRf5W'

WEBHOOK_HOST =
'https://hubuz.onrender.com" WEBHOOK_PATH =f (API_TOKEN)'
WEBHOOK_URL = f"(WEBHOOK_HOST) [WEBHOOK_PATH)"
WEBAPP_HOST ="0.0.0.0 WEBAPP PORT = R int(os.getenv('PORT, 8O)

logging.basicConfig(level=lo gging.INFO)
bot =
Bot(token=APL_TOKEN) dp = Dispatcher(bot) dp.middleware.setup(Loggin gMiddleware())
@dp.message
handler(commands=['start", 'help'])
async def
send_welcome(message: types.Message): await
message.reply("Salom! Men sizga UC sotib olishda yordam beruvchi botman.")

async def on_startup(dp): await bot.set_webhook(W EBHOOK_URL)
async def on_shutdown(dp): await
bot.delete_webhook()
if- name --' start_webhook( dispatcher=dp,
main
webhook_path=WEBHO OK_PATH,
on_startup=on_startup, on_shutdown=on_shutd
own,
host=WEBAPP_HOST, port=WEBAPP_PORT,
    )
`
