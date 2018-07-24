from telegram.ext import CommandHandler
from telegram.ext import Updater
from text_summarizer import summarizer


def summarize_reply(bot, update):
    return summarizer.schematize(update.message.reply_to_message.text)

def start_message(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Text summarization bot. Done by Fran Rodrigo.')


def percentage_message(bot, update):
    # Set error message
    error_msg = 'Incorrect value. Please send a floating point number in the range [0 - 1] (i.e. 0.5).'

    if len(update.message.text) > 4:
        try:
            pct = float(update.message.text[5:].encode('utf-8'))
            if 0.0 <= pct <= 1.0:
                summarizer.percentage = pct
                bot.sendMessage(chat_id=update.message.chat_id, text='Percentage setted :)')

        except ValueError:
                bot.sendMessage(chat_id=update.message.chat_id, text=error_msg)

    else:
        bot.sendMessage(chat_id=update.message.chat_id, text=error_msg)


def tldr_message(bot, update):
    if update.message.reply_to_message is not None:
        bot.sendMessage(chat_id=update.message.chat_id, text=summarize_reply(bot, update))

    if len(update.message.text) > 5:
        text = update.message.text[6:].encode('utf-8')
        summ = summarizer.schematize(text)
        bot.sendMessage(chat_id=update.message.chat_id, text=summ)


with open('token.txt') as f:
    token = f.readlines()[0]

updater = Updater(token=token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start_message)
dispatcher.add_handler(start_handler)

percentage_handler = CommandHandler('pct', percentage_message)
dispatcher.add_handler(percentage_handler)

tldr_handler = CommandHandler('tldr', tldr_message)
dispatcher.add_handler(tldr_handler)

updater.start_polling()
