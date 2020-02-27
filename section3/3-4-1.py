from bs4 import BeautifulSoup
import sys
import io
import requests, json
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# Session 생성, with구문 안에서 유지
with requests.Session() as s :
    # 게시글 가져오기
    post_one = s.get('https://bbs.ruliweb.com/hobby/board/300142/read/30591432?')
    # 예외발생
    post_one.raise_for_status()
    # 예외 발생 print()
    # print(post_one.status_code)
    # print(post_one.ok)


    soup = BeautifulSoup(post_one.text,'html.parser')
    print(soup)
    issue = soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > div > p")
    for i in issue:
        print(i.string)

    #$print(issue.string)
