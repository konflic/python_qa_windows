import os
import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver


def test_upload_guru99(driver):
    driver.get('http://demo.guru99.com/test/upload/')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'selenium.png')
    input_manager = driver.find_element_by_css_selector('input#uploadfile_0')
    input_manager.send_keys(filename)
    driver.find_element_by_id("submitbutton").click()
    time.sleep(10)


def test_upload_radical(driver):
    driver.get('https://radikal.ru')
    uploader = driver.find_element_by_class_name("upload1")
    filename = os.path.join(os.path.dirname(__file__), 'selenium.png')
    uploader.send_keys(filename)
    time.sleep(10)
