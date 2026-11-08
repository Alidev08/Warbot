import os
import telebot
from dotenv import load_dotenv

# خوندن توکن از فایل .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# اتصال به ربات
bot = telebot.TeleBot(TOKEN)

# جواب دادن به دستور /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات بازی خوش اومدی. 🎮\nمن آماده‌ام که بازی رو شروع کنیم!")

# اگه کاربر چیز دیگه‌ای نوشت
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "فعلا فقط دستور /start کار می‌کنه.")

print("ربات روشن شد... برو توی تلگرام تستش کن!")
bot.infinity_polling()

