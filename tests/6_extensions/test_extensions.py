import time
import pytest
import os 

from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    filename = os.path.join(os.path.dirname(__file__), "adblock.crx")
    options.add_extension(filename)
    driver = webdriver.Chrome(options=options)
    driver.get("https://konflic.github.io/examples/")
    
    yield driver
    
    driver.close()


def test_disabled_button(browser):
    time.sleep(10)
