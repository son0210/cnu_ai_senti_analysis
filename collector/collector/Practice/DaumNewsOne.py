# 파이썬의 경로
# 1. 프로젝트(cnu_senti_analysis-main)
# └ 2. python package(collector)
#   └ 3. python file(test.py, DaumNewsOne.py)
# - python package: python file들을 모아둔 폴더 (폴더 아이콘 안에 구멍 뚫려 있음)

# import와 library(module)
# - python 코드를 직접 작성해서 개발할 수도 있지만,
# - 다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# - 이미 개발 되어 있는 코드들의 묶음 = library(module)
#  1. built in library : Python 설치하면 자동으로 제공 (ex: math, sys, os 등)
#  2. 위부 library : 직접 추가해서 사용! (ex: requests, beautifulsoup4 등)
#
# Library를 사용하기 위해서 import 작업 진행
# - import는 도서관에서 필요한 책을 빌려 오는 개념

import requests  # 책 전체를 빌려옴
from bs4 import BeautifulSoup  # bs4라는 책에서 BeautifulSoup 1개 파트만 빌려옴

# 목표 : Daum 뉴스 웹 페이지의 제목과 본문 데이터를 수집!
# 1. url : https://v.daum.net/v/20221006104711611
url = 'https://v.daum.net/v/20221006104711611'
# 2. requests로 해당 url의 html 전체 코드를 수집!
result = requests.get(url)
# print(result.text)
# 3. BeautifulSoup을 통해서 '제목과 본문'만 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python에서 [] : List Type
# index  0  1  2  3   4
#     - [5, 6, 9, 10, 15] : List 내에는 다양한 데이터 저장 가능
title = doc.select('h3.tit_view')[0].get_text()  # h3 태그 중에 이름이 tit_view를 갖는 select

# html -> tag + 선택자
#  - tag : 기본적으로 정의 돼있음 (h3, p, div, span, ...)
contents = doc.select('section p')  # section 태그를 부모로 둔 모든 자식 p 태그를 select

print(f'뉴스 제목 : {title}')

# contents = [<p1>, <p2>, <p3>, <p4>, ...] : 복수의 본문 포함

# 반복적인 작업 -> for문
content = ''
for line in contents:  # 순서대로 <p>를 가져와서 line에 넣고 다음 코드 실행
     content += line.get_text()
print(f'뉴스 본문: {content}')
