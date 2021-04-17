import time

from config import CHROMEDRIVER
from selenium import webdriver


chrome = webdriver.Chrome(CHROMEDRIVER)
chrome.maximize_window()
chrome.get("https://konflic.github.io/front_example/pages/iframes.html")

# Получаем iframe элементы на странице
frames = chrome.find_elements_by_css_selector("iframe")

# Переключаемся в первый iframe в списке
chrome.switch_to.frame(frames[0])
chrome.find_element_by_name("search").send_keys("MacBook")
chrome.find_element_by_xpath("//*[@id='search']//button[@type='button']").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element_by_id("main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

# Переключаемся в iframe по имени
chrome.switch_to.frame("selenium")
chrome.find_element_by_id("dropdownButton").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element_by_id("main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

# Переключаемся по порядковому номеру
chrome.switch_to.frame(2)
chrome.find_element_by_id("state").send_keys("fg;lsadkjg;lsakjdg;lksaj")
chrome.find_element_by_css_selector("#submit").click()
# Возвращаемся в исходный контекст
chrome.switch_to.default_content()
chrome.find_element_by_id("main").click()
chrome.switch_to.alert.accept()
time.sleep(2)

chrome.close()
