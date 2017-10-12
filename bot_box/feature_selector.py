from bot_box.bot_constants import *
from bot_box.features import joke_me, quote_me, animate_me, image_me, chat_me, bot_info

FILE_TAG = globals()["__name__"]


# TODO: use regular expression instead of string matching

def get_feature(user_input=""):
    """
    this determines the feature of the bot and fetch the response from its api
    :param user_input:
    :return: the response in the text form (either message or url) or None
    """
    _input = user_input
    user_input = user_input.lower().replace(BOT_NAME, "").strip()
    if user_input == "":
        return None
    elif user_input.startswith("help"):  # help
        return None

    elif user_input.startswith("joke me"):  # joke me
        return joke_me.joke_me_api()

    elif user_input.startswith("quote me"):  # quote me
        return quote_me.quote_me_api()

    elif user_input.startswith("animate me"):  # animate me
        query = user_input.replace("animate me", "").strip()
        return animate_me.animate_me_api(query)

    elif user_input.startswith("image me"):  # image me
        query = user_input.replace("image me", "").strip()
        return image_me.image_me_api(query)

    elif user_input.startswith("info"):
        query = user_input.replace("info", "").strip()
        query = query.replace('<', '').replace('@', '').replace('>', '').strip()
        print("\n\n\nquery: ", query)
        if query.__len__() != 9:
            return None
        return bot_info.bot_info_api(query)


    # elif user_input.startswith(""):                               # (some cool function) me
    #     return None   # return as you want

    else:  # chat with me
        if _input.strip().strip().startswith(BOT_NAME):
            _input = _input.replace(BOT_NAME, "", 1)
        _input = _input.replace(BOT_NAME, ONLINE_CHATBOT_NAME1)
        return chat_me.ONLINE_CHATBOT_RESP(_input)
