from bot_box.features import requests, json, os


def joke_me_api():
    while True:
        try:
            url = os.environ.get('JOKE_URL')
            joke_resp_raw = requests.get(url).text
            joke_resp = json.loads(joke_resp_raw)
            if joke_resp and 'attachments' in joke_resp:
                joke = joke_resp['attachments'][0]['text']
                return joke
        except Exception as e:
            print(e)
