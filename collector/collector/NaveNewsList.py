import requests
from bs4 import BeautifulSoup

url ='https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'

headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, Liek Gecko) Chrome/92.8.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)


doc = BeautifulSoup(result.text, 'html.parser')
title_list = doc.select('ul.type86_headline li')
print(len(title_list))

# 못 갖고 와잉...네이버가 막아놓음
