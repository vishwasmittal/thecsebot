from bot_box.features import json, bsp, request, parse, os
from bot_box.bot_constants import *

# CHATBOT_URL = os.environ.get('CHATBOT_URL')
CHATBOT_BOTCUST2 = os.environ.get("CHATBOT_BOTCUST2")


def ONLINE_CHATBOT_RESP(user_input):
    """
        gets the user input and contact our online chatbot in this case A.L.I.C.E.
        to get the natural language response from it and returns the response, the
        the response mai contain "ALICE" or "A.LI.C.E." replace it properly
        :param user_input: the input of user to be fed to chat bot
        :return: the response given by chat bot
    """
    url = 'https://www.pandorabots.com/pandora/talk?botid=a847934aae3456cb'
    botcust2 = CHATBOT_BOTCUST2
    headers = {"Content-Type": "application/x-www-form-urlencoded", 'user-agent': USER_AGENT}
    req = request.Request(url, headers=headers)
    datadict = {'botcust2': botcust2, 'input': user_input}
    data = parse.urlencode(datadict)
    data = data.encode('ascii')

    resp = request.urlopen(req, data)
    alice_resp = resp.read().decode()
    soup = bsp(alice_resp, 'html.parser')
    lines = soup.text.split('\n')
    respond = lines[10]
    if lines[10] is not "": respond += lines[11]
    respond = respond.replace(ONLINE_CHATBOT_NAME2 + ": ", "")
    respond = respond.split("   ")[0]
    respond = respond.replace(CHATBOT_CREATER, BOT_CREATER)
    return respond
