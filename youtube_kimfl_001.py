import urllib.request
from bs4 import BeautifulSoup

# 고정 url
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_="title_link _cross_trigger")

for i in title:
    print(i.attrs['href'])