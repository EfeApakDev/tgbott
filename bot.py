from flask import Flask, request, jsonify
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

app = Flask(__name__)

TOKEN = os.getenv('7267318470:AAG0PgGQTVqHwdjLWdO4vieguGIoPdXxr_I')
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    update = Update.de_json(data, updater.bot)
    dispatcher.process_update(update)
    return jsonify(success=True)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot çalışıyor!')

dispatcher.add_handler(CommandHandler('start', start))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
