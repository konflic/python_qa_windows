import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


@pytest.fixture
def browser():
    # wd = webdriver.Chrome()
    wd = webdriver.Firefox()
    yield wd
    wd.quit()


def test_basic_alert(browser):
    browser.get("https://konflic.github.io/front_example/pages/alerts.html")
    browser.find_element_by_id("basic").click()
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    browser.find_element_by_id("prompt").click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    # Для хрома не работает
    prompt.send_keys('Hello, from selenium!')
    time.sleep(2)
    prompt.accept()

    browser.find_element_by_id("confirm").click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    print(confirm.text)
    confirm.accept()
    time.sleep(2)
