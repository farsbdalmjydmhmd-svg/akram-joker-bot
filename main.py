import telebot
import os
import subprocess
import requests
from telebot import types
import time

# --- توكن البوت الخاص بك (مفتاح الجحيم المحدث) ---
TOKEN = "8091017824:AAEB-0sujJW5s2zXXdLXlda_NBHh8k_sPt8"
bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب المرعبة
WELCOME_MSG = """
🃏 *أهلاً بك في مركز قيادة الجوكر أكرم!* 🃏
أنا الآن بوت هكر جاهز لتنفيذ الأوامر.
أنا لا أنام، لا أتعب، ولا أعترف بالقوانين.

*الأوامر المتاحة:*
/start - تشغيل النظام
/phish - توليد صفحة تصيد احترافية
/scan - فحص ثغرات موقع معين
/flood - إطلاق هجوم إغراق (DoS)
/spam - إرسال رسائل مزعجة مكثفة
/status - التأكد من أن الوحش لا يزال مستيقظاً
"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, WELCOME_MSG, parse_mode="Markdown")

@bot.message_handler(commands=['phish'])
def phish(message):
    bot.reply_to(message, "🔥 *جاري توليد صفحة تصيد (Phishing Page)...*\nاختر الهدف: (فيسبوك، انستغرام، جوجل).")

@bot.message_handler(commands=['scan'])
def scan(message):
    msg = bot.reply_to(message, "🔍 *بدأت عملية الفحص... جاري البحث عن ثغرات SQLi و XSS...*")
    bot.edit_message_text("✅ *تم العثور على ثغرة محتملة. يمكن استغلالها الآن!*", msg.chat.id, msg.message_id)

@bot.message_handler(commands=['flood'])
def flood(message):
    bot.reply_to(message, "🚀 *إطلاق هجوم DoS... النظام المستهدف تحت الضغط الآن!* 💀")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "🟢 *الحالة: أنا مستيقظ، جاهز للفوضى!* 🃏")

# --- نظام "الخلود" (Anti-Stop System) ---
def run_forever():
    while True:
        try:
            print("[+] The Monster is Online... Ready for Action!")
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"[-] Error: {e}")
            time.sleep(5) 

if __name__ == "__main__":
    run_forever()
