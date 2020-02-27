import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver = webdriver.Chrome('D:/atom_python/section3/webdriver/chrome/chromedriver')
driver.get('https://google.com')
driver.save_screenshot('D:/atom_python/section3/webdriver/chrome/website2.png')
driver.quit()
