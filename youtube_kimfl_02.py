# 네이버 VIEW 검색 크롤링

import urllib.request
import urllib.parse  # 한글 주소를 변환하는 모듈
from bs4 import BeautifulSoup

baseUrl = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
plusUrl = input("검색어를 입력하세요: ")
url = baseUrl + urllib.parse.quote_plus(plusUrl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_="title_link _cross_trigger")

for i in title:
    print(i.attrs['href'])