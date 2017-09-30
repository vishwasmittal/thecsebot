import requests
import json


def joke_me_api():
    while True:
        try:
            url = "https://icanhazdadjoke.com/slack"
            joke_resp_raw = requests.get(url).text
            joke_resp = json.loads(joke_resp_raw)
            if joke_resp and 'attachments' in joke_resp:
                joke = joke_resp['attachments'][0]['text']
                return joke
        except Exception as e:
            print(e)
