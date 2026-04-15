import telebot
from flask import Flask
from threading import Thread

# التوكن الخاص بك مدمج مباشرة للتجربة
API_TOKEN = '8712768972:AAE8dfEe8TM7WAJm3F6i6r9sU9fURnLHFRc'

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً يحيى! البوت شغال الآن على ريندر بأفضل أداء 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

if name == "main":
    keep_alive() # تشغيل السيرفر الوهمي لإرضاء Render
    print("البوت بدأ العمل...")
    bot.infinity_polling()
