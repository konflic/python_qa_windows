import pytest
import time

from helpers import there_is_window_other_than
from selenium import webdriver
from config import CHROMEDRIVER
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    wd = webdriver.Chrome(executable_path=CHROMEDRIVER)
    wd.get("https://konflic.github.io/front_example/")
    yield wd
    wd.quit()


def test_windows_manual(browser):
    main_window = browser.current_window_handle
    old_windows = browser.window_handles

    browser.execute_script('window.open();')  # открывает новое окно
    new_window = WebDriverWait(browser, 2).until(there_is_window_other_than(old_windows))
    browser.switch_to.window(new_window)
    browser.get("https://yandex.ru")

    time.sleep(2)
    browser.close()
    browser.switch_to.window(main_window)
    browser.find_element_by_id("myBtn").click()

    time.sleep(2)
    browser.close()


def test_windows_with_link(browser):
    main_window = browser.current_window_handle
    old_windows = browser.window_handles

    browser.find_element_by_link_text("New window").click()
    new_window = WebDriverWait(browser, 2).until(there_is_window_other_than(old_windows))
    assert new_window, "Новое окно не открылось после клика по ссылке"
    browser.switch_to.window(new_window)
    browser.get("https://yandex.ru")

    time.sleep(2)
    browser.close()
    browser.switch_to.window(main_window)

    time.sleep(2)
    browser.close()
