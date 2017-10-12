from slack_bot.models import SlackUser
from django.shortcuts import get_object_or_404


def bot_info_api(query):
    user = get_object_or_404(SlackUser, uid=query)
    return user.name