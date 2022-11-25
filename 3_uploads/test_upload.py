import os
import pytest
import time

from selenium.webdriver.common.by import By

from config import CHROMEDRIVER
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    driver.implicitly_wait(10)
    def fin(): driver.quit()
    request.addfinalizer(fin)
    return driver


def test_upload_radical(driver):
    driver.get('https://konflic.github.io/examples/editor/index.html')
    uploader = driver.find_element(By.CSS_SELECTOR, "#file-uploader")
    filename = os.path.join(os.path.dirname(__file__), 'selenium.png')
    uploader.send_keys(filename)
    time.sleep(10)
