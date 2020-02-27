from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html,"html.parser")
links = soup.find_all("li")
a = soup.find("li")
print('prettify',soup.prettify())
lis = soup.select(".lecs>li")
print(lis)
for li in lis:
    print('li = ',li.string)
