# 구글 검색결과 크롤링

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요?: ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

r = soup.select('.yuRUbf')
for i in r:
    print(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
    print(i.select_one('.byrV5b').text)
    print(i.a.attrs['href'])
    print()

driver.close()