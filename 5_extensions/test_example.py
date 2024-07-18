import time
import pytest

from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_extension("ublock.crx")
    options.add_extension("ad-blocker.crx")
    driver = webdriver.Chrome(options=options)
    driver.get("https://konflic.github.io/examples/")
    yield driver
    driver.close()


def test_disabled_button(browser):
    time.sleep(5)
