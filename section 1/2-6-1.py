from bs4 import BeautifulSoup
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")
html = """
<html><body>
    <ul>
        <li id="naver"><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
soup = BeautifulSoup(html,"html.parser")
s = soup.find(id="naver").string  #find(id="naver") 가능 select(id="naver") 불가능
print(s)
li = soup.find_all(href=re.compile(r"^http://"))
print(li)
