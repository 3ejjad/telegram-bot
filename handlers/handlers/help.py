from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("دستورهای موجود:\n/start - شروع ربات\n/help - راهنما")
