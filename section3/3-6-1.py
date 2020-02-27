import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver = webdriver.PhantomJS('D:/atom_python/section3/webdriver/phantomjs/phantomjs')

driver.implicitly_wait(5)
driver.get('http://google.com')
driver.save_screenshot("D:/atom_python/section3/webdriver/phantomjs/website1.png")

print("스크린샷 완.")
