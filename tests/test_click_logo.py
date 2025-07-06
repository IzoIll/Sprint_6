import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from tests.data import UrlsData, TextData

@pytest.mark.usefixtures("driver")
class TestLogo:
    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    @allure.description('На странице заказа нажать на логотип "Самокат", выполнен переход на главную страницу Самоката')
    def test_main_page_open_by_scooter_logo(self, driver):
        order_pages = BasePage(driver)
        order_pages.open_page(UrlsData.Order_scooter_url)
        pages = MainPage(driver)
        pages.click_scooter_logo()
        current_header_text = MainPage(driver).get_main_header_text()
        header_text = TextData.Header_text
        assert driver.current_url == UrlsData.Scooter_url and header_text == current_header_text

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    @allure.description('На странице заказа нажать на логотип "Яндекс", выполнен переход на страницу Дзен')
    def test_dzen_page_open_by_yandex_logo(self, driver):
        order_pages = BasePage(driver)
        order_pages.open_page(UrlsData.Order_scooter_url)
        pages = MainPage(driver)
        pages.click_yandex_logo()
        assert UrlsData.Dzen_url not in driver.current_url