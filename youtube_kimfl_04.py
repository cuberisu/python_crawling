# 인스타그램 태그검색 이미지 크롤링
# 인스타는 자바스크립트로 되어 있어 selenium이 필요하다.

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time


baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input("검색할 태그를 입력하세요: ")
url = baseUrl + quote_plus(plusUrl)  # 한글을 ASCII Code로 변환

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

insta = soup.select('._aabd._aa8k._al3l')

n = 1
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    imgUrl = i.select_one('._aagv').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()