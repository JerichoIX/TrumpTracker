# ***************************************************************************************
# TRUMP CRAWLER PROJECT - v1.0
# By B. Derakhshan
#
# ---------------------------------------------------------------------------------------
#
# 'Romanov' spider:
# Scrapes the CNN website for news on Donald Trump. Searches the URL specified below to
# retrieve the latest 25 articles on Trump.
#
# ---------------------------------------------------------------------------------------
#
# SYSTEM PARAMETERS - DO NOT ALTER!
# --------------------------------
URL = 'http://us.cnn.com/politics'
PAUSE_TIME = 3

# Import required libraries
import time
from selenium import webdriver

URL = 'http://us.cnn.com/politics'
                                        # The URL the spider will scrape
PAUSE_TIME = 3
                                        # How long should the scraper wait for the site
                                        # to load
# ***************************************************************************************

def romanov():
    start_time = time.time()
    driver = webdriver.PhantomJS()
    driver.get(URL)
    #print("Got URL!")

    while True:
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Check if the page height has remained the same
        if new_height == last_height:
            # If so, we are done
            break
        # If not, move on to the next loop
        else:
            last_height = new_height
            continue

    #print('Fetching done!')
    html1 = driver.page_source
    #html2 = driver.execute_script("return document.documentElement.innerHTML;")

    #print(type(html1))
    with open('politics.html', 'wb') as f:
        f.write(str.encode(html1))
    end_time = time.time()
    elapsed = int(end_time-start_time)
    print("Elapsed time: "+ str(elapsed))
    return str(elapsed)