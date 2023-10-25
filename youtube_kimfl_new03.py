# 네이버 VIEW 검색 스크롤 크롤링

from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

keyword = input("검색어를 입력하세요: ")

search_url = base_url + keyword

driver = webdriver.Chrome()
driver.get(search_url)

time.sleep(3)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # javascript 문법
    time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".title_link._cross_trigger")  # 앞에를. 공백도 .으로 바꾼다

# for e, item in enumerate(items, 1):
#     print(f"{e}: {item.text}")

items = soup.select(".view_wrap")  # 앞에를 .으로 바꾼다

for rank, item in enumerate(items, 1):
    print(f"<<{rank}>>")
    ad = item.select_one(".link_ad")
    if ad:
        print("광고입니다.")
        continue
    blog_title = item.select_one(".name").text
    print(f"{blog_title}")
    post_title = item.select_one(".title_link._cross_trigger")
    print(f"{post_title.text}")
    print(f"{post_title.get('href')}")
    # print(f"{post_title['href']}")
    print( )

driver.quit()