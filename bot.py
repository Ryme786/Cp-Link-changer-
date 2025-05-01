from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me a link, and I'll modify it for you!")

def modify_link(update: Update, context: CallbackContext) -> None:
    original_link = update.message.text.strip()
    if original_link.startswith("http"):
        modified_link = f"https://api.extractor.workers.dev/player?url={original_link}"
        update.message.reply_text(f"Here's your modified link:\n{modified_link}")
    else:
        update.message.reply_text("Please send a valid link.")

def main():
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    TOKEN = "7875684141:AAE3J_t2Lk_fvK02G9B1FkO6zjiLwVXomHA"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, modify_link))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
