# ***************************************************************************************
# TRUMP CRAWLER PROJECT - v1.0
# By B. Derakhshan
#
# ---------------------------------------------------------------------------------------
#
# 'Banner' parser:
# Parses the data retrieved from CNN and lists the latest 25 articles about Trump, and
# their URLs.
#
# ---------------------------------------------------------------------------------------
#
# CONFIGURATION
# --------------

MAX_ARTICLES = 25
                                        # The maximum number of articles retrieved


# SYSTEM PARAMETERS - DO NOT ALTER!
# ---------------------------------

URL = 'https://us.cnn.com/politics'
                                        # The URL the spider will scrape
BASE_URL = 'https://us.cnn.com'
                                        # Used to complete the href link addresses
LINK_FORMATS = [
    '/2018',
    'https://www.cnn.com/politics/',
    'https://www.cnn.com/specials/politics/'
]

PASTEBIN_API_DEV_KEY = '5702d2d815da2bf784a46f222f705678'

PASTEBIN_USERNAME = 'markthewraith@gmail.com'

PASTEBIN_PASS = 'Wraithmaster47'


# ***************************************************************************************

# Import libraries
from bs4 import BeautifulSoup
import json

def banner():

    with open('politics.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Parse the CNN page to find the Trump-related articles
    headers = soup.find_all('h3', attrs={'class': 'cd__headline'})
    titles = []
    links = []
    counter = 0

    for header in headers:
        temp = header.find('span', attrs={'class': 'cd__headline-text'})

        # Filter out the irrelevant entries
        # We only want the articles which contain the word 'Trump'
        if 'Trump' in temp.text:

            # Found a match!
            counter += 1

            # Add the article title to our list
            titles.append(temp.text)

            # The links have one of these formats:
            #     '/2018/...'
            #     'https://www.cnn.com/politics/...'
            #     'https://www.cnn.com/specials/politics/...'
            # We modify the links with the first format to produce an absolute path
            temp = header.find('a', href=True)['href']
            if 'www.cnn.com' in temp:
                links.append(temp)
            else:
                links.append(BASE_URL + temp)

        if counter >= MAX_ARTICLES:
            break

    # Build a dict variable to write the results in JSON format
    result = {}
    for title in titles:
        # We are sure that no two articles have the exact same titles, so we can use
        # the following approach to enumerate over the titles list
        i = titles.index(title)
        result[title] = links[i]


    return json.dumps(result)

