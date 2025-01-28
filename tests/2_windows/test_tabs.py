import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def there_is_window_other_than(windows):
    """
    :param windows: Массив из окон
    :return: Дескриптор нового окна
    """

    def wrapped(driver):
        new_win = driver.window_handles
        if len(new_win) > len(windows):
            return list(set(new_win).difference(windows))[0]
        else:
            return False

    return wrapped


@pytest.fixture
def browser():
    wd = webdriver.Chrome()
    wd.get("https://konflic.github.io/examples/")
    yield wd
    wd.quit()


def test_windows_manual(browser):
    main_window = browser.current_window_handle
    old_windows = browser.window_handles
    browser.execute_script('window.open();')  # открывает новое окно
    new_window = WebDriverWait(browser, 2).until(there_is_window_other_than(old_windows))
    browser.switch_to.window(new_window)
    browser.get("https://ya.ru")
    time.sleep(2)
    browser.close()
    browser.switch_to.window(main_window)
    browser.find_element(value="myBtn").click()
    time.sleep(2)
    browser.close()


def test_windows_with_link(browser):
    main_window = browser.current_window_handle
    old_windows = browser.window_handles
    browser.find_element(By.LINK_TEXT, "New window").click()
    new_window = WebDriverWait(browser, 2).until(there_is_window_other_than(old_windows))
    assert new_window, "Новое окно не открылось после клика по ссылке"
    browser.switch_to.window(new_window)
    browser.get("https://ya.ru")
    time.sleep(2)
    browser.close()
    browser.switch_to.window(main_window)
    time.sleep(2)
    browser.close()
