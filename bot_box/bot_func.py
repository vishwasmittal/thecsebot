import os
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))
BOT_ID = os.environ.get("BOT_ID")


def send_message(channel=None, text=None):
    print(slack_client.rtm_connect())
    a = slack_client.api_call("chat.postMessage", channel=channel, text=text, as_user=True)
    print('a:', a)


# can also do all the things using api directly, no need to engage bot...
# example: https://slack.com/api/chat.postMessage
# for more info refer to https://api.slack.com/methods

if __name__ == "__main__":
    send_message('C5QLDE198', 'Hello!! this is just a test, no need to be afraid :smile:')
