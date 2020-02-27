import requests,json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


r = requests.get("https://api.github.com/events")
# r.raise_for_status()

jar=requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies')

r=requests.get('https://httpbin.org/cookies',cookies=jar)
r.raise_for_status()
print(r.text)

#Fake Reset : test에 성공하면 메시지 변환(실제로 처리되지 않음)
r=requests.post('https://httpbin.org/post',data=payload)
payload1={'key1':'name1','key2':'name'}
r=requests.post('https://httpbin.org/post',data=payload1)
