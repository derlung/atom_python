import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)
    def __init__(self) :
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r"D:/atom_python/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    def writeAttendCheck(self) :
        #로그인
        self.driver.get("https://cafe.naver.com/hby")
        self.driver.find_element_by_xpath('//*[@id="gnb_login_button"]').click()
        self.driver.implicitly_wait(1)
        self.copy_input('//*[@id="id"]','zxxs1105')
        self.driver.implicitly_wait(1)
        self.copy_input('//*[@id="pw"]','rkdxotks1')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(1)
        self.driver.implicitly_wait(1)

        #멤버 화면 가져오기
        self.driver.get("https://cafe.naver.com/nby/CafeMemberViewTab.nhn?defaultSearch.clubid=10135947")
        self.driver.implicitly_wait(1)
        self.driver.switch_to.frame('cafe_main')
        soup =  BeautifulSoup(self.driver.page_source,'html.parser')
        members = soup.select("div.ellipsis.m-tcol-c")
        return members



    def copy_input(self,xpath,input):
            pyperclip.copy(input)
            self.driver.find_element_by_xpath(xpath).click()
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            time.sleep(1)

    def printMemberList(self,list):
        print(list)

    # 소멸자 (생성자를 닫아주는 역활)
    # def __del__(self) :
    #     self.driver.quit()
    #
    #

ns = NcafeWriteAtt()
ns.printMemberList(ns.writeAttendCheck())
