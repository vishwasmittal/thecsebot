from bot_box.features import requests, bsp, os  # imported in __init__.py

''' Sample Response

        <forismatic>
        <quote>
            <quoteText>Don't miss all the beautiful colors of the rainbow looking for that pot of gold.</quoteText>
            <quoteAuthor></quoteAuthor>
            <senderName></senderName>
            <senderLink></senderLink>
        <quoteLink>
'''


def quote_me_api():
    """
    relsult of quote command of user
    :return: the quote and its author
    """
    # TODO: include this url in .env file
    url = os.environ.get('QUOTE_URL')
    while True:
        quote_resp = requests.get(url).text
        soup = bsp(quote_resp, 'html.parser')
        quote = soup.find('quote')
        text = quote.find('quotetext').get_text()
        author = quote.find('quoteauthor').get_text()
        return "" + text + "\n- " + author
