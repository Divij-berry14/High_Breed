import urllib
import requests
from google_play_scraper import app
from google_play_scraper import Sort, reviews
# import play_scraper
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import re
# result=app('com.nianticlabs.pokemongo',
#     lang='en', # defaults to 'en'
#     country='us' # defaults to 'us'
# )

# print(play_scraper.details('com.android.chrome'))
# print(play_scraper.collection(
#         collection='TRENDING',
#         category='GAME_RACING',
#         results=5,
#         page=1))
myfile=open("3.txt","w")
url="https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers&hl=en_IN"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup)
title=soup.title
print_title=title.string
print(title.string)
# print(type(title))
paras=soup.find("meta",itemprop='description')
# print(type(paras))
# print(len(paras))
print_des=paras["content"]
# print(paras["content"])
rating=soup.find("div",class_="BHMmbe")
print_rating=rating.string
print(rating.string)
downloads=soup.find("span",class_="AYi5wd TBRnV")
print_downloads=downloads.text
print(downloads.text)
developer_name=soup.find("a",class_="hrTbp R8zArc")
print_developer_name=developer_name.text
print(developer_name.text)
print("Reviews")
result = reviews(
    'com.fantome.penguinisle',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=1, # defaults to 100
    filter_score_with=5 # defaults to None(means all score)
)
print_result=''.join(d['content'] for d in result)
print(print_result)
print(result)
# print_result="".join(result)
# print(print_result)
myfile.write(print_title)
myfile.write(print_rating)
myfile.write(print_result)
myfile.write(print_developer_name)
myfile.write(print_downloads)
myfile.write(print_des)
myfile.close()
# print("Reviews")
# review_name=soup.find("span",class_="zc7KVe")
# print(review_name.text)
# review_des=soup.find("span",jsname="fbQN7e")
# print(review_des.text)

