class StartHandler(object):
    """
    Class for handling /start messages
    """

    @staticmethod
    def start_message(bot, update):
        """
        Respond to /start messages
        :param bot: The bot instance
        :param update: The message received
        :return: The response
        """
        bot.sendMessage(chat_id=update.message.chat_id, text='Text summarization bot. Done by Fran Rodrigo.')
