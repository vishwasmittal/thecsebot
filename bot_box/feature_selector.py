from bot_box.features import joke_me


def get_feature(text="", user=None, channel=None):
    return joke_me.joke_me_api()
