import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

s = requests.session()
r = s.get('http://naver.com') #get(가져오기), post(업데이트), put(입력), delete(삭제)


# test메세지를 보내고 응답을 받음

# url = 'http://httpbin.org/get'
# headers={'user-agent':'mypythonApp_1.0.0'}
# r = s.get(url,headers=headers)
# print(r.text)
# s.close()

with requests.session() as s:
    r=s.get('http://naver.com')
    print(r.text)

payload:cookies={'from':'myname'}
r=s.get('http://httpbin.org/cookies',cookies={'from':'myname'})
print('2',r.text)
