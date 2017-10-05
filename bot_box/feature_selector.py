from bot_box.bot_constants import *
from bot_box.features import joke_me, quote_me, animate_me, image_me


# TODO: use regular expression instead of string matching

def get_feature(user_input=""):
    user_input = user_input.lower().replace(BOT_NAME, "").strip()
    if user_input == "":
        return None
    elif user_input.startswith("help"):                             # help me
        return None  # Bot help

    elif user_input.startswith("joke me"):                          # joke me
        return joke_me.joke_me_api()

    elif user_input.startswith("quote me"):                         # quote me
        return quote_me.quote_me_api()

    elif user_input.startswith("animate me"):                      # animate me
        query = user_input.replace("animate me", "").strip()
        return animate_me.animate_me_api(query)

    elif user_input.startswith("image me"):                         # image me
        query = user_input.replace("image me", "").strip()
        return image_me.image_me_api(query)

    # elif user_input.startswith(""):                               # (some cool function) me
    #     return None   # return as you want


    else:                                                           # chat with me
        user_input = BOT_NAME + " " + user_input
        return None  # return the response of chatbot
