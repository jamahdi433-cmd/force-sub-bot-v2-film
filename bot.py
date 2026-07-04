import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("8914306340:AAFpHy9xYEik5TCyn721iEq7Xc4uW1_VkCI")
CHANNEL = "configkarmania"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL}")],
        [InlineKeyboardButton("✅ Check Join", callback_data="check")]
    ]

    await update.message.reply_text(
        "برای استفاده از ربات باید اول عضو کانال بشی 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    member = await context.bot.get_chat_member(f"@{CHANNEL}", user_id)

    if member.status in ["member", "administrator", "creator"]:
        await query.message.edit_text("✅ خوش آمدی! الان می‌تونی از ربات استفاده کنی.")
    else:
        await query.answer("❌ هنوز عضو نشدی!", show_alert=True)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check))

    app.run_polling()

if __name__ == "__main__":
    main()
