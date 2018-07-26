from text_summarizer import summarizer


class PercentageHandler(object):
    """
    Class for handling /pct messages
    """

    @staticmethod
    def percentage_message(bot, update):
        """
        Respond to /pct messages
        :param bot: The bot instance
        :param update: The message received
        :return: The response
        """
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

