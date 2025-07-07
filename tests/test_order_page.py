import pytest
from Data.data import RentalData, TextData, OrdersData, UrlsData
from pages.base_page import BasePage
from pages.order_page import OrderPages

@pytest.mark.fixture('driver')
class TestOrderButton:

    def test_order_button_on_header(self, driver):
        page = BasePage(driver)
        page.open_page(UrlsData.Scooter_url)
        order_pages = OrderPages(driver)
        order_pages.click_cookie_button()
        order_pages.click_order_button_in_header()
        order_pages.create_order(OrdersData.Order_1)
        order_pages.click_next_button()
        order_pages.input_rental_information(RentalData.Data_1)
        order_pages.wait_for_confirm()
        order_pages.click_confirmation_order()
        order_title = order_pages.get_new_order_title()
        order_pages.wait_for_order_completed()
        assert TextData.Successful_order_text in order_title

    def test_order_button_on_footer(self, driver):
        page = BasePage(driver)
        page.open_page(UrlsData.Scooter_url)
        order_pages = OrderPages(driver)
        order_pages.click_cookie_button()
        order_pages.click_order_button_in_header()
        order_pages.create_order(OrdersData.Order_2)
        order_pages.click_next_button()
        order_pages.input_rental_information(RentalData.Data_2)
        order_pages.wait_for_confirm()
        order_pages.click_confirmation_order()
        order_title = order_pages.get_new_order_title()
        order_pages.wait_for_order_completed()
        assert TextData.Successful_order_text in order_title