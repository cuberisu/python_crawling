# 네이버 VIEW 검색 크롤링

from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

keyword = input("검색어를 입력하세요: ")

search_url = base_url + keyword

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.select(".title_link._cross_trigger")  # 앞에를. 공백도 .으로 바꾼다

for e, item in enumerate(items, 1):
    print(f"{e}: {item.text}")