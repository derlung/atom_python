
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(res,'html.parser')

popular = soup.select("ul#popularItemList>li")

print("네이버 주식 인기검색 종목 10위")
for i,e in enumerate(popular,1):
    print("순위 :",i,", 이름 :",e.select_one("a").string)
