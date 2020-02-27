
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,'html.parser')

print("실시간 이슈 검색어")
issue = soup.select("div.realtime_part li")
for i,e in enumerate(issue,1):
    print(i,":",e.select_one("a").string)
