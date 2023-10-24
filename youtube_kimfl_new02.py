from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

keyword = input("검색어를 입력하세요: ")

search_url = base_url + keyword

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")

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