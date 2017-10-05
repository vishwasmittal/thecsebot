from bot_box.features import requests, bsp  # imported in __init__.py

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
    # TODO: include this url in .env file
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=xml&lang=en"
    while True:
        quote_resp = requests.get(url).text
        soup = bsp(quote_resp, 'html.parser')
        quote = soup.find('quote')
        text = quote.find('quotetext').get_text()
        author = quote.find('quoteauthor').get_text()
        return "" + text + "\n- " + author
