from bot_box.features import requests, os


def joke_me_api():
    """
    result of joke command of user
    :return: joke in the form of text
    """
    while True: # retries if there is any error
        try:
            url = os.environ.get('JOKE_URL')
            joke_resp_raw = requests.get(url).json()
            # joke_resp = json.loads(joke_resp_raw)
            if joke_resp and 'attachments' in joke_resp:
                joke = joke_resp['attachments'][0]['text']
                return joke
        except Exception as e:
            print(e)
