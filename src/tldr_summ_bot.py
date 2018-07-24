from telegram.ext import CommandHandler
from telegram.ext import Updater
from text_summarizer import summarizer


def start_message(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Text summarization bot. Done by Fran Rodrigo.")


def tldr_message(bot, update):
    if len(update.message.text) > 5:
        text = update.message.text[6:]
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=summarizer.schematize(text))

with open('token.txt') as f:
    token = f.readlines()[0]

updater = Updater(token=token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start_message)
dispatcher.add_handler(start_handler)

tldr_handler = CommandHandler('tldr', tldr_message)
dispatcher.add_handler(tldr_handler)



updater.start_polling()