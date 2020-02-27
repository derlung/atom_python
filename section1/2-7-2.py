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

top = soup.select("#siselist_tab_0 > tr .tltle")
top2 = soup.select("#siselist_tab_0 > tr ")

# for e in top:
#     print(e.string)

# for i,e in enumerate(top):
#     print(i,e)
#     if e.find("a") is not None:
#         print(i,e.select_one(" .tltle").string)
#
# for i,e in enumerate(top):
#     print(i+1,e.string)
#
# #
# # i = 1
# # for e in top2:
# #     if e.find("a") is not None:
# #         print(i,e.select_one(".tltle").string)
# #         i+=1
# v = 0
# for i,e in enumerate(top2,1):
#     if e.find("a")!=None:
#         print(i-v,".",e.select_one(".tltle").string)
#     else:
#         v+=1


# v=0
# print('Top 10 현재가 출력')
# for i,e in enumerate(top2,1):
#     if e.find("a")!=None:
#         pass
#         print(i-v,".",e.select_one(".tltle").string,"=",e.select_one("td:nth-of-type(5)").string)
#     else:
#         v+=1

popular = soup.select("ul.popularItemList")
