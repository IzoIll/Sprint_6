import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()