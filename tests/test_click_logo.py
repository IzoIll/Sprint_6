import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from Data.data import UrlsData, TextData
from locators.locators import MainPageLocators

@pytest.mark.usefixtures("driver")
class TestLogo:
    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    @allure.description('На странице заказа нажать на логотип "Самокат", выполнен переход на главную страницу Самоката')
    def test_main_page_open_by_scooter_logo(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.open_page(UrlsData.Order_scooter_url)
        main_page.click_scooter_logo()
        current_header_text = BasePage(driver).get_main_header_text(MainPageLocators.Header_text)
        assert driver.current_url == UrlsData.Scooter_url and TextData.Header_text == current_header_text

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    @allure.description('На странице заказа нажать на логотип "Яндекс", выполнен переход на страницу Дзен')
    def test_dzen_page_open_by_yandex_logo(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.open_page(UrlsData.Order_scooter_url)
        main_page.click_yandex_logo()
        assert UrlsData.Dzen_url not in driver.current_url