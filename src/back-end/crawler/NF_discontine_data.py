"""crawling discontinue data for Netflix"""

import os

from selenium import webdriver

# 실행한 웹 사이트
URL = "https://www.naver.com/"
print(__file__)
print(os.getcwd())
driver_path = "\\chromewebdrive\\chromedrive_win32\\chromedriver.exe"
# 하...시발 이거 os가 mac인지 윈도우인지도 확인해줘야해???
print(driver_path)
path = os.getcwd() + driver_path
print(path)
driver = webdriver.Chrome(path)
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)
driver.close()
