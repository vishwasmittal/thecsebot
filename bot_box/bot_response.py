from bot_box.features import joke_me
from _datetime import datetime

BOT_ID = 'U7BHJS4F7'
AT_BOT = '<@' + BOT_ID + '>'
prev_message_time = 0
print("globals()['prev_message_time']: ", globals()['prev_message_time'])


def get_response(event_time, user_input="", user=None, channel=None):
    """
    to decide get the response for the bot
    :param user_input: the input given bu the user
    :param user: who given the input
    :param channel: which channel
    :param event_time: the time when the event occurred
    :return: response of bot
    """

    curr_message_time = event_time
    print("globals()['prev_message_time']: ", globals()['prev_message_time'])
    print('curr_message_time: ', curr_message_time)
    if globals()['prev_message_time'] < curr_message_time + 1:
        globals()['prev_message_time'] = curr_message_time
        if user == BOT_ID:
            return None
        elif user_input.startswith(AT_BOT):
            return "sample response"

    return None

# 'bot: <@U7BHJS4F7>,,,,,,,,,,, bottesting: <#C5QLDE198|bottesting> ,,,,,,,,,,, vishwas: <@U3SRS5L59>'
