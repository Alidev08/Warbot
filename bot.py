import os
import telebot
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# خوندن توکن از فایل .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# اتصال به ربات
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به ربات بازی خوش اومدی. 🎮\nمن آماده‌ام که بازی رو شروع کنیم!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "فعلا فقط دستور /start کار می‌کنه.")

# --- بخش وب سرور برای رندر ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    print("ربات روشن شد... برو توی تلگرام تستش کن!")
    bot.infinity_polling()
