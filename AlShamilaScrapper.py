from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from datetime import datetime
import re

chromrdriver = "C:/Users/mutla/PycharmProjects/fantasy-art-master/scrapper/chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
            'Accept-Language': 'en-US, en;q=0.5'})

url = 'https://shamela.ws/book/samplebook'  ## the url of the first page you would like to scrape.

s = ''
while True:
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    div = soup.find('div', class_ = 'nass margin-top-10')
    for p in div.find_all('p'):
        s+=p.get_text()
    page = soup.find('input', class_ = 'text-center')['value']
    s+='\n Page '+page+'\n'
    page = int(page)
    if page >= 364: ### the number of the last page of the book you want to scrape 
        break
    else:
        driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[2]/div[6]/div/a[3]').click() # finding element that contains 'GET' in it and click it
        url = driver.current_url
with open("BookName.txt", "w",encoding='utf-8') as text_file:
    text_file.write(s)