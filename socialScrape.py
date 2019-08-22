"""
This program takes a users input of a URL and scrapes their website to attempt to find
either their facebook page and twitter page.

"""


from bs4 import BeautifulSoup
import requests
import time
import re

#https://www.desmoinesregister.com/ Test Domain

site_url= input("""Please Enter the name of the website you would like to find social
                media sites for""")
global site_url
pattern = re.compile("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")
print (pattern.match(site_url))
 


def scrapeContent(url):
    print('waiting for 1 second!')
    time.sleep(1)
    # add headers
    page = requests.get(url, headers= headers)
    page_content = page.content
    # parse the page through the BeautifulSoup library
    soup = BeautifulSoup(page_content, "html.parser")
    url_content = soup.find_all('a')
    for social_link in url_content:
      try:
        clean_link = (social_link.get('href'))
        if "twitter" in clean_link.lower():
          twitter_url = clean_link.lower()
          print("Congrats! Here is your Twitter link: " + clean_link)
          #print(len(twitter_url))
          if "?" in twitter_url.lower():
            continue
          row = { 'url': url,
                    'Facebook': facebook_url,
                    'Twitter': twitter_url}
          rows.append(row)
        if "facebook" in clean_link.lower():
          facebook_url = clean_link.lower()
          #print(len(facebook_url))
          if "?" in facebook_url.lower():
            continue
          print("Congrats! Here is your Facebook link: " + clean_link)
          row = { 'url': url,
                    'Facebook': facebook_url,
                    'Twitter': twitter_url}
      except:
        continue
        #print("There was an exception here for Facebook: Please Debug.")


scrapeContent(site_url)
