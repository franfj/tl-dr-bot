class StartHandler(object):
    """
    Class for handling /start messages
    """

    @staticmethod
    def start_message(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text='Text summarization bot. Done by Fran Rodrigo.')

