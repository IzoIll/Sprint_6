import pytest
from selenium import webdriver
from Data.data import UrlsData

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(UrlsData.Order_scooter_url)
    yield driver
    driver.quit()