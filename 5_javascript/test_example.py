import time
import pytest

from selenium import webdriver
from config import CHROMEDRIVER
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    wd = webdriver.Chrome(executable_path=CHROMEDRIVER)
    wd.get("https://konflic.github.io/front_example/")
    return wd


def test_disabled_button(browser):
    browser.get("https://konflic.github.io/front_example")
    browser.maximize_window()

    # Сначала проверяем клик по задизейбленой кнопке
    dis_btn = browser.find_element_by_id("disabled")

    dis_btn.click()

    time.sleep(1)  # Для демонстрации

    # Проверяем что не видна модалка
    WebDriverWait(browser, 3).until_not(EC.visibility_of(browser.find_element_by_id("myModal")))

    #  Убираем атрибут через js и проверяем
    js_code = "$('#disabled')[0].disabled = false;"
    browser.execute_script(js_code)

    time.sleep(1)  # Для демонстрации

    dis_btn.click()

    time.sleep(1)  # Для демонстрации

    # Проверяем что видна модалка
    WebDriverWait(browser, 3).until(EC.visibility_of(browser.find_element_by_id("myModal")))
