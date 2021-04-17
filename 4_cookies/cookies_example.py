import time

from config import CHROMEDRIVER
from selenium import webdriver


chrome = webdriver.Chrome(CHROMEDRIVER)
chrome.get("https://yandex.ru")

cookies = chrome.get_cookies()

for cookie in cookies:
    print(cookie["name"], cookie["value"])

chrome.delete_all_cookies()

chrome.quit()