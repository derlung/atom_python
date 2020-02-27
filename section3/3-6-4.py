# import sys
# import io
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#
# chrome_option=Options()
# chrome_option.add_argument("--headless")#CLI
# driver = webdriver.Chrome(chrome_options=chrome_option,executable_path=r'D:/atom_python/section3/webdriver/chrome/chromedriver')
# driver.get('https://google.com')
# driver.quit()
import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests

#import time
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# chrome_option=Options()
# chrome_option.add_argument("--headless")   # CLI

        # 요청
driver = webdriver.Chrome(executable_path=r'D:/atom_python/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://www.wishket.com/accounts/login/')
driver.find_element_by_name('identification').send_keys('tessan22')
driver.find_element_by_name('password').send_keys('rkdtks12')
driver.find_element_by_xpath('//*[@id="submit"]').click()
