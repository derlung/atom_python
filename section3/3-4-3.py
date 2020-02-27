import requests
from bs4 import BeautifulSoup
import requests
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#Session 생성,with구문 안에서 유지
with requests.Session()as s:

    #권한이 필요한 게시판 게시글 가져오기
    post_one = s.get('https://movie.naver.com/movie/bi/mi/point.nhn?code=187321')
    # 예외발생
    post_one.raise_for_status()
    #예외처리
    #BeautifulSoup 선언
    soup = BeautifulSoup(post_one.text,'html.parser')
    critic = soup.select("div.score_result li")
    rate = soup.select("div.score_result div.star_score > em")
    name = soup.select("div.score_result div.score_reple dd")

    print("-- 평론가 비평 --")
    for i in range(len(critic)):
         print("{} 평론가 - 평점:{} , {}".format(name[i].getText().split()[1],rate[i].string,critic[i].select_one("p").string))
