# 프로그램 실행되는 곳 >> 필요한 기능들 호출해서 사용!
from collector.collector_naver_movie_review import movie_review_crawler

movie_code = '207037'  # 네이버 영화 코드
movie_review_crawler(movie_code)



