import allure
import pytest
from pages.main_page import MainPage
from Data.data import UrlsData

@pytest.mark.usefixtures("driver")
class TestLogo:
    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    @allure.description('На странице заказа нажать на логотип "Самокат", выполнен переход на главную страницу Самоката')
    def test_main_page_open_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert current_url == UrlsData.Scooter_url

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    @allure.description('На странице заказа нажать на логотип "Яндекс", выполнен переход на страницу Дзен')
    def test_dzen_page_open_by_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        current_url = main_page.get_current_url()
        assert UrlsData.Dzen_url not in current_url