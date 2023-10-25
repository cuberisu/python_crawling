# 네이버 VIEW 검색 여러 페이지 크롤링

import urllib.request
import urllib.parse  # 한글 주소를 변환하는 모듈
from bs4 import BeautifulSoup

plusUrl = urllib.parse.quote_plus(input("검색어를 입력하세요: "))
i = input('몇페이지 크롤링 할까요?: ')

pageNum = 1
count = 1
lastPage = int(i) * 10 - 9

while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all(class_="title_link")
    print(f'-----{count}페이지 결과입니다-----')

    for i in title:
        print(i.attrs['href'])
    print()
    
    pageNum += 10
    count += 1