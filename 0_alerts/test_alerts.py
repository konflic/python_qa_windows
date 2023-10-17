import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


@pytest.fixture
def browser():
    service = Service()
    wd = webdriver.Chrome(service=service)
    # wd = webdriver.Firefox(executable_path=GECKODRIVER)
    wd.get("https://konflic.github.io/examples/pages/alerts.html")
    yield wd
    wd.quit()


def test_basic_alert(browser):
    time.sleep(1)
    browser.find_element(By.ID, "basic").click()
    time.sleep(1)
    alert = WebDriverWait(browser, 2).until(EC.alert_is_present())
    alert.accept()
    time.sleep(1)


def test_prompt_alert(browser):
    time.sleep(1)
    browser.find_element(By.ID, "prompt").click()
    prompt_alert = browser.switch_to.alert
    # Для хрома не работает
    prompt_alert.send_keys('Hello, from selenium!')
    time.sleep(1)
    prompt_alert.accept()
    time.sleep(2)


def test_confirm_alert(browser):
    time.sleep(2)
    browser.find_element(By.ID, "confirm").click()
    confirm_alert = browser.switch_to.alert
    print(confirm_alert.text)
    confirm_alert.accept()
    time.sleep(2)


def test_custom_alert(browser):
    browser.find_element(By.CSS_SELECTOR, "a.button").click()
    WebDriverWait(browser, 1).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.popup")))
    time.sleep(2)  # Для демонстрации
    browser.find_element(By.CSS_SELECTOR, "a.close").click()
    WebDriverWait(browser, 1).until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, "div.popup")))
    time.sleep(2)  # Для демонстрации
