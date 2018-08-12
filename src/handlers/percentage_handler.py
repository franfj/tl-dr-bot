from firebase import firebase

from src import FIREBASE_URL


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
        error_msg = 'Incorrect value. Please send a floating point number in the range [0 - 0.5] (i.e. 0.15).'

        if len(update.message.text) > 4:
            try:
                pct = float(update.message.text[5:].encode('utf-8'))
                if 0.0 <= pct <= 1.0:
                    user_id = update.message.from_user.id

                    db = firebase.FirebaseApplication(FIREBASE_URL, None)

                    # Delete old value, and add new one
                    db.delete(str(user_id), None)
                    db.post(str(user_id), pct)

                    bot.sendMessage(chat_id=update.message.chat_id, text='Percentage setted :)')

            except AttributeError:
                bot.sendMessage(chat_id=update.message.chat_id, text=error_msg)

            except ValueError:
                bot.sendMessage(chat_id=update.message.chat_id, text=error_msg)

        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=error_msg)
