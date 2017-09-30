from features.joke_me import joke_me_api


def get_feature(text="", user=None, channel=None):
    return joke_me_api()
