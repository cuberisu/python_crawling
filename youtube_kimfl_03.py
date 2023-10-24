# 네이버 이미지검색 크롤링

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input("검색어를 입력하세요: ")
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all('img')


n = 1
for i in img:
    imgUrl = i['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
print("다운로드 완료")
