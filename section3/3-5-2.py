from bs4 import BeautifulSoup
import requests
import urllib.request as req
import sys
import io,json
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#다음 주식 요청 url
# print(request.get_method()) #Post or Get 확인
# print(request.get_full_url()) #요청 Full Url 확인
#요청
ua=UserAgent()
headers= {'User-Agent':ua.ie,'Referer':'https://finance.daum.net/'}
url="https://finance.daum.net/api/search/ranks?limit=10"
res = req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')
#확인(jason data)
print('res',res)
#응답 데이터 str - json 변환 및 data 값 저장
rank_json = json.loads(res)['data']
#중간확인
print("중간 확인",rank_json,'\n')
for elm in rank_json:
    #print(type(elm)) #Type 확인
    print('{}위 {}원 회사명 : {}'.format(elm['rank'],elm['tradePrice'],elm['name']))
