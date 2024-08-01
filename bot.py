from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Bot token'ınızı çevre değişkenlerinden alır
TOKEN = os.getenv('7267318470:AAG0PgGQTVqHwdjLWdO4vieguGIoPdXxr_I')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot çalışıyor!')

def main():
    # Updater ve Dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Komut işleyiciler
    dp.add_handler(CommandHandler("start", start))

    # Botu başlat
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
