from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("8712768972:AAEnxBdz3jpgzU7TgTWDgBvhEnXies8-2UE")

broker_link = "https://your-broker-link.com"
transfer_link = "https://your-transfer-link.com"
vip_group_link = "https://t.me/yourvipgroup"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في بوت التوصيات 📈\n\n"
        "اكتب:\n"
        "- عندي خلفية\n"
        "- بدي أبدأ من الصفر\n"
        "- كيف أنضم للمجموعة الثانية\n"
        "- بدي أنقل الوكالة"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if any(word in text for word in ["خلفية", "خبرة", "بعرف"]):
        await update.message.reply_text(f"رابط الوكالة 👇\n{broker_link}")

    elif any(word in text for word in ["من الصفر", "مبتدئ", "تعلم"]):
        await update.message.reply_text(
            "ابدأ بالأساسيات 👌\n"
            "- الشموع\n"
            "- إدارة رأس المال\n"
            "- الدعم والمقاومة\n\n"
            f"رابط البداية:\n{broker_link}"
        )

    elif any(word in text for word in ["المجموعة", "vip", "انضم"]):
        await update.message.reply_text(f"رابط المجموعة 👇\n{vip_group_link}")

    elif any(word in text for word in ["نقل", "وكالة"]):
        await update.message.reply_text(f"رابط نقل الوكالة 👇\n{transfer_link}")

    elif any(word in text for word in ["نقلت", "حولت"]):
        await update.message.reply_text("ممتاز ✅ ابعت رقم حسابك للتحقق.")

    else:
        await update.message.reply_text("اكتب سؤالك بشكل واضح 🙏")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot started successfully ✅")
app.run_polling()
