from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os.path
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


areatxt = 'D:/atom_python/areaNumber.txt'
area = open(areatxt,'r').read()
area1 = area.split("\n")
search = input("날씨를 확인하고 싶은 지역을 입력해주세요 : ").split("\n")
a=""
for an in area1:
    if(search[0]==an[:-12]):
        a=an[-11:-1]
        break
    elif(search[0]+" "==an[:-12]):
        a=an[-11:-1]
        break
    elif(search[0]+"  "==an[:-12]):
        a=an[-11:-1]
        break
    else:
        pass
url="http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone="+a
savename = 'D:/atom_python/section4/GwangMyeong_forecast.xml'

#
# if not os.path.exists(savename) :
req.urlretrieve(url, savename)
#
#
#BeautifulSoup으로 분석
xml = open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml,"html.parser")


savefile = 'D:/atom_python/section4/GwangMyeong_forecast.txt'
with open(savefile,"wt",encoding="utf-8") as f:
    f.write("위치 : "+soup.find("category").string+"\n")
    data = soup.find_all("data")
    day = -1
    now =  datetime.datetime.now()
    for d in data:
        if(day != (int)(d.find("day").string)):
            f.write("==================================\n")
            day = (int)(d.find("day").string)
            now = now + datetime.timedelta(days=1)
            f.write(now.strftime('%Y-%m-%d')+"\n")
        f.write(d.find("hour").string+" 시 - ")
        f.write(d.find("wfkor").string+"\n")
    f.write("==================================\n")
