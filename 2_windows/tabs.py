import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    return webdriver.Chrome()


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


def test_windows(browser):
    browser.get("https://konflic.github.io/front_example/")
    main_window = browser.current_window_handle
    old_windows = browser.window_handles

    browser.execute_script('window.open();')  # открывает новое окно
    # https://selenium-python.readthedocs.io/waits.html
    new_window = WebDriverWait(browser, 2).until(there_is_window_other_than(old_windows))
    browser.switch_to.window(new_window)
    browser.get("https://yandex.ru")

    time.sleep(2)
    browser.close()
    browser.switch_to.window(main_window)

    time.sleep(2)
    browser.close()
