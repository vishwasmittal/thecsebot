from django.shortcuts import render

from slack_bot.models import SlackUser


def index(request):
    return render(request, 'bot_site/index.html')


def members(request):
    return render(request, 'bot_site/members.html')


def contact(request):
    return render(request, 'bot_site/contact.html')

