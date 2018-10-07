from bot_box.features import requests
from django.shortcuts import get_object_or_404
from slack_bot.models import SlackUser


def joke_other_api(query):
    user = get_object_or_404(SlackUser, uid=query.upper())
    print(user)
    name = user.name

    try:
        first_name = name.split(" ")[0]
        last_name = name.split(" ")[1]
    except IndexError:
        first_name = name
        last_name = ""

    """
    result of joke command of user ponting to other
    :return: joke in the form of text
    """
    while True:  # retries if there is any error
        try:
            url = "http://api.icndb.com/jokes/random?firstName=%s&lastName=%s" % (first_name, last_name)
            joke_resp = requests.get(url).json()
            if joke_resp and joke_resp['type'] == "success":
                joke = joke_resp['value']['joke']
                html_entities = {'&quot;' : '\"',
                                 '&aspo;' : '\'',
                                 '&amp;'  : '&' } #Add acording to need
                
                for data,replacement in html_entities.iteritems():
                    joke = joke.replace(data,replacement)

                return joke
        except Exception as e:
            print(e)
