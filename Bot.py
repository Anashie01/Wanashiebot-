import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Bot is live!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
