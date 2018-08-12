from telegram.ext import CommandHandler
from telegram.ext import Updater

from get_resources_info import BOT_TOKEN
from handlers import StartHandler, PercentageHandler, TldrHandler

# Init updater & dispatcher
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

# Add handlers to dispatcher
start_handler = CommandHandler('start', StartHandler.start_message)
dispatcher.add_handler(start_handler)

percentage_handler = CommandHandler('pct', PercentageHandler.percentage_message)
dispatcher.add_handler(percentage_handler)

tldr_handler = CommandHandler('tldr', TldrHandler.tldr_message)
dispatcher.add_handler(tldr_handler)

# Start listening
updater.start_polling()
