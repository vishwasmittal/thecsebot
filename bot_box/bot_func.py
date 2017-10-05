import os
from slackclient import SlackClient

from bot_box.bot_response import get_response

slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))
BOT_ID = os.environ.get("BOT_ID")


def send_message(event_time, user_input="", user=None, channel=None):
    """
    selects the feature for a a given user_input and send the forwards the response to slack using bot
    :param user_input: the message sent by users on the slack
    :param user: who sent the message
    :param channel: where message is sent
    :param event_time: the time when the event occurred
    :return: the same response that is forwarded using bot
    """

    response = get_response(user_input=user_input, user=user, channel=channel, event_time=event_time)
    if response is not None and slack_client.rtm_connect():
        a = slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
        # print('\n\na:', a)
        return a  # if the message is successfully sent
    return ""















# if __name__ == "__main__":
#     send_message(channel='C5QLDE198', user_input='Hello!! this is just a test, no need to be afraid :smile:')

# can also do all the things using api directly, no need to engage bot...
# example: https://slack.com/api/chat.postMessage
# for more info refer to https://api.slack.com/methods
