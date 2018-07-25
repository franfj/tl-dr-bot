from telegram.ext import CommandHandler
from telegram.ext import Updater

from handlers import StartHandler, PercentageHandler, TldrHandler

with open('token.txt') as f:
    token = f.readlines()[0]

updater = Updater(token=token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', StartHandler.start_message)
dispatcher.add_handler(start_handler)

percentage_handler = CommandHandler('pct', PercentageHandler.percentage_message)
dispatcher.add_handler(percentage_handler)

tldr_handler = CommandHandler('tldr', TldrHandler.tldr_message)
dispatcher.add_handler(tldr_handler)

updater.start_polling()
