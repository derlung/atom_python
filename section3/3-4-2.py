import requests
from bs4 import BeautifulSoup
import requests
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

LOGIN_INFO ={
'user_id':'tessan22',
'user_pw':'rkdtks12'
}

#Session 생성,with구문 안에서 유지
with requests.Session()as s:
    login_req=s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)
    #HTML 소스 확인
    print('login_req :',login_req.headers)

    #Response 정상 확인
    if login_req.status_code == 200 and login_req.ok:
        print("로그인 성공")
        #권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('https://mypi.ruliweb.com/mypi.htm?num=8035&nid=7231')
        # 예외발생
        post_one.raise_for_status()
        #예외처리
        #BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text,'html.parser')
        issue = soup.select("#mypiRead div.story>p")
        for p in issue:
            print(p.string)
