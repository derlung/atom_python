import requests
from bs4 import BeautifulSoup
import requests
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#Session 생성,with구문 안에서 유지
with requests.Session()as s:

    #Response 정상 확인
    print("로그인 성공")
    #권한이 필요한 게시판 게시글 가져오기
    post_one = s.get('http://www.cgv.co.kr/movies/detail-view/?midx=83022#commentReg')
    # 예외발생
    post_one.raise_for_status()
    #예외처리
    #BeautifulSoup 선언
    soup = BeautifulSoup(post_one.text,'html.parser')
    issue = soup.select("#liCommentFirst29796262")
    print(issue)
