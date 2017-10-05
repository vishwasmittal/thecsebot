from bot_box.features import joke_me
from bot_box.feature_selector import get_feature
from _datetime import datetime
from bot_box.bot_constants import *

FILE_TAG = globals()["__name__"]

prev_message_time = 0


def get_response(event_time, user, user_input="", channel=None):
    """
    this function will do some pre-processing of the message and apply the necessary checks
    :param user_input: the input given bu the user
    :param user: who given the input
    :param channel: which channel
    :param event_time: the time when the event occurred
    :return: response of bot
    """

    curr_message_time = event_time
    if globals()['prev_message_time'] < curr_message_time + 1:
        # prevents sending a message multiple times using the time of the event at which it occurred
        globals()['prev_message_time'] = curr_message_time
        if user == BOT_ID or user == SLACKBOT_ID or user_input.strip() == "":
            # no response to messages sent by bot itself, slackbot or empty messages
            return None
        elif user_input.__contains__(AT_BOT):
            # here pre-process the message
            # like convert @bot into the BOT_NAME
            user_input = user_input.strip().replace(AT_BOT, BOT_NAME)
            response = get_feature(user_input=user_input)
            return response
    return None

# 'bot: <@U7BHJS4F7>,,,,,,,,,,, bottesting: <#C5QLDE198|bottesting> ,,,,,,,,,,, vishwas: <@U3SRS5L59>'
