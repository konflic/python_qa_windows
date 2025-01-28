import os
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from drag_and_drop import drag_and_drop_file


@pytest.fixture
def driver(request):
    options = Options()
    prefs = {"download.default_directory": os.path.join(os.path.dirname(__file__))}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
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


def test_download(driver):
    driver.get('https://konflic.github.io/examples/editor/index.html')
    driver.find_element(By.CSS_SELECTOR, "#editor_text").send_keys("test_" * 10)
    driver.find_element(By.CSS_SELECTOR, "#save_file").click()
    time.sleep(3)
