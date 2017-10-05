from bot_box.bot_constants import *
from bot_box.features import joke_me, quote_me


# TODO: use regular expression instead of string matching

def get_feature(user_input=""):
    user_input = user_input.lower().replace(BOT_NAME, "").strip()
    if user_input == "":
        return None
    elif user_input.startswith("help"):
        return None  # Bot help

    elif user_input.startswith("joke me"):
        return joke_me.joke_me_api()

    elif user_input.startswith("quote me"):
        return quote_me.quote_me_api()

    elif user_input.startswith("animate me"):
        query = user_input.replace("animate me", "").strip()
        return None  # return the animation for given query

    elif user_input.startswith("image me"):
        query = user_input.replace("image me", "").strip()
        return None  # return image

    # elif user_input.startswith(""):
    #     return None   # return as you want


    else:
        user_input = BOT_NAME + " " + user_input
        return None  # return the response of chatbot
