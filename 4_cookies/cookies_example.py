from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("https://yandex.ru")

# cookies = chrome.get_cookies()

saved_cookie = chrome.get_cookie("mda")
saved_cookie["value"] = "0873247234723472984723098174092381740923874"

chrome.add_cookie(cookie_dict=saved_cookie)

chrome.quit()