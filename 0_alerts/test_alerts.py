import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import CHROMEDRIVER, GECKODRIVER
import selenium.webdriver.support.expected_conditions as EC


@pytest.fixture
def browser():
    # wd = webdriver.Chrome(executable_path=CHROMEDRIVER)
    wd = webdriver.Firefox(executable_path=GECKODRIVER)
    wd.get("https://konflic.github.io/front_example/pages/alerts.html")
    yield wd
    wd.quit()


def test_basic_alert(browser):
    time.sleep(1)
    browser.find_element_by_id("basic").click()
    time.sleep(1)
    WebDriverWait(browser, 2).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)


def test_prompt_alert(browser):
    time.sleep(1)
    browser.find_element_by_id("prompt").click()
    prompt_alert = browser.switch_to.alert
    # Для хрома не работает
    prompt_alert.send_keys('Hello, from selenium!')
    time.sleep(1)
    prompt_alert.accept()
    time.sleep(2)


def test_confirm_alert(browser):
    time.sleep(2)
    browser.find_element_by_id("confirm").click()
    confirm_alert = browser.switch_to.alert
    print(confirm_alert.text)
    confirm_alert.accept()
    time.sleep(2)
