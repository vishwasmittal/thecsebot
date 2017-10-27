from bot_box.features import requests#, os NOT needed now
from django.shortcuts import get_object_or_404
from slack_bot.models import SlackUser

def joke_other_api(query):
    # Get Details of other user. Copied from bot_info
    user = get_object_or_404(SlackUser, uid=query.upper())
    name = user.name

    try:
        firstName = name.split(" ")[0]
        lastName = name.split(" ")[1]
    except IndexError:
        firstName = name
        lastName = ""
    
    """
    result of joke command of user ponting to other
    :return: joke in the form of text
    """
    while True: # retries if there is any error
        try:
            # TODO: Add url in environment variable
            # url = os.environ.get('JOKE_URL')
            url = "http://api.icndb.com/jokes/random?firstName=%s&lastName=%s" % (firstName,lastName)
            joke_resp = requests.get(url).json()
            if joke_resp and joke_resp['type']=="success":
                joke = joke_resp['value']['joke']
                return joke
        except Exception as e:
            print(e)
