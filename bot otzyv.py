from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8509181702:AAFQL65EuVGqGsivAtYHx0PfWc3mSNL-ICs"
LINK = "https://example.com"  # 👈 СІЛТЕМЕ

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("▶️ Старт")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Сәлем сайтқа өту үшін старт батырмасын бас 👇",
        reply_markup=reply_markup
    )

async def handle_start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "▶️ Старт":
        await update.message.reply_text(LINK)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_start_button)
)

print("✅ Бот іске қосылды")
app.run_polling()


