import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

firefox_option=Options()
firefox_option.add_argument("--headless")#CLI

driver = webdriver.Firefox(firefox_options=firefox_option,executable_path=r'D:/atom_python/section3/webdriver/firefox/geckodriver.exe')
driver.get("https://google.com")
driver.save_screenshot("D:/atom_python/section3/webdriver/firefox/website2.png")
