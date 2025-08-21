from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
from handlers import start, help, echo

def main():
    updater = Updater(config.TOKEN)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start.start))
    dp.add_handler(CommandHandler("help", help.help_command))

    # Message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo.echo))

    # Run the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
