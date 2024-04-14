import os
import pytest
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from uploads_3.drag_and_drop import drag_and_drop_file


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    def fin(): driver.quit()
    request.addfinalizer(fin)
    return driver


def test_upload(driver):
    driver.get('https://konflic.github.io/examples/editor/index.html')
    uploader = driver.find_element(By.CSS_SELECTOR, "#file-uploader")
    filename = os.path.join(os.path.dirname(__file__), 'selenium.png')
    time.sleep(1)
    uploader.send_keys(filename)
    time.sleep(3)


def test_dnd_upload(driver):
    driver.get('https://konflic.github.io/examples/pages/upload_files_dnd.html')
    uploader = driver.find_element(By.CSS_SELECTOR, "#drop-area")
    filename = os.path.join(os.path.dirname(__file__), 'selenium.png')
    time.sleep(1)
    drag_and_drop_file(uploader, filename)
    time.sleep(3)
