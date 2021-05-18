import time

from config import CHROMEDRIVER
from selenium import webdriver


chrome = webdriver.Chrome(CHROMEDRIVER)
chrome.get("https://yandex.ru")

cookies = chrome.get_cookies()

for cookie in cookies:
    print(cookie["name"], cookie["value"])

chrome.delete_all_cookies()

time.sleep(5)

# Yandex restore some cookies
cookies_after_delete = chrome.get_cookies()

chrome.quit()