import urllib
import requests
from google_play_scraper import app
from google_play_scraper import Sort, reviews
import play_scraper
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import re
# result=app('com.nianticlabs.pokemongo',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )
# result = reviews(
#     'com.fantome.penguinisle',
#     lang='en', # defaults to 'en'
#     country='us', # defaults to 'us'
#     sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
#     count=3, # defaults to 100
#     filter_score_with=5 # defaults to None(means all score)
# )
# print(result)
print(play_scraper.details('com.android.chrome'))
print(play_scraper.collection(
        collection='TRENDING',
        category='GAME_RACING',
        results=5,
        page=1))
# url="https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers&hl=en_IN"
# r=requests.get(url)
# htmlcontent=r.content
# soup=BeautifulSoup(htmlcontent,'html.parser')
# # print(soup)
# title=soup.title
# print(title.string)
# print(type(title))
# soup = BeautifulSoup(urllib.urlopen(url))
# for link in soup.findAll('a'):
#         print(link.string)
# print(htmlcontent)
# driver=webdriver.Chrome("F:\chromedriver.exe")
# driver.get("https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers&hl=en_IN")
# response=driver.execute_script("return document.documentElement.outerHTML")
#
# soup=BeautifulSoup(response,'lxml')
# print(soup.prettify)
# print(scraper.details('com.android.chrome'))
