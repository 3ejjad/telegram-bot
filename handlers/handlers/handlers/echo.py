from telegram import Update
from telegram.ext import CallbackContext

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"پیام تو: {text}")
