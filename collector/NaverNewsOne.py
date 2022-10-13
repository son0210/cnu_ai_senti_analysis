import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/052/0001799371?sid=103'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, Liek Gecko) Chrome/92.8.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')

# python > '', "" 상관X
title = doc.select('h2.media_end_head_headline')[0].get_text()
# get_text() : 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백을 제거
content = doc.select('div#dic_area')[0].get_text().strip()
print(f'본문: {title}')  # fstring (최근 방식)
print('내용: {}'.format(content))  # format (옛날 방식)
