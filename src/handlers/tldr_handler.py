import os

import validators
from text_summarizer import summarizer

from tools import UrlGrabber


class TldrHandler(object):
    """
    Class for handling /tldr messages
    """

    @staticmethod
    def summarize_reply(update):
        input_text = update.message.reply_to_message.text
        text = TldrHandler.check_for_url(input_text)  # Search for url's
        return summarizer.schematize(text)

    @staticmethod
    def tldr_message(bot, update):

        # Summarize reply messages
        if update.message.reply_to_message is not None:
            bot.sendMessage(chat_id=update.message.chat_id, text=TldrHandler.summarize_reply(update))

        # Summarize common messages
        elif len(update.message.text) > 5:
            input_text = update.message.text[6:].encode('utf-8')
            text = TldrHandler.check_for_url(input_text)  # Search for url's
            summ = summarizer.schematize(text)
            bot.sendMessage(chat_id=update.message.chat_id, text=summ)

    @staticmethod
    def check_for_url(text):
        if validators.url(text):
            if os.path.splitext(text)[1] == '.pdf':
                return UrlGrabber.get_text_from_first_page_pdf(text)

            else:
                return UrlGrabber.get_text_from_url(text)

        return text
