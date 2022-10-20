import requests
from bs4 import BeautifulSoup
from collector.Practice.CollectorService import get_daum_news

url = 'https://news.daum.net/breakingnews/digital'
# SSL Error → requests.get
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

# <a href='url' : a 태그는 클릭 했을 때 해당 url로 이동
# len() : List[]의 갯수를 알려 주는 함수
title_list = doc.select('ul.list_news2 a.link_txt')
# pprint.pprint(title_list)
# print(len(title_list))

# enumerate() : 반복 하면서 index 번호와 item 가져옴
# List[]의 index는 0번부터 시작
# Len(List) = 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'인덱스: {i+1}, url: {title["href"]}')  # 속성이 href인 것만 추출
    get_daum_news(title["href"])  # 뉴스 제목, 본문 수집 함수
