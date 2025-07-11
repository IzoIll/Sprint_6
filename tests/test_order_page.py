import  allure
import pytest
from Data.data import RentalData, TextData, OrdersData
from pages.order_page import OrderPages
from locators.locators import OrderPageLocators

@pytest.mark.fixture('driver')
class TestOrderButton:
    @allure.title('Заказ самокатов с двумя позитивными сценариями')
    @allure.description('Первый заказ самоката с вводом данных. Самокат заказан успешно, отображается номер заказа')
    def test_order_button_on_header(self, driver):
        order_pages = OrderPages(driver)
        order_pages.click_cookie_button_order()
        order_pages.click_order_button_in_header()
        order_pages.create_order(OrdersData.Order_1)
        order_pages.click_next_button()
        order_pages.input_rental_information(RentalData.Data_1)
        order_pages.wait_for_confirm(OrderPageLocators.Confirm)
        order_pages.click_confirmation_order()
        order_title = order_pages.get_new_order_title(OrderPageLocators.Order_completed)
        order_pages.wait_for_order_completed(OrderPageLocators.Order_completed)
        assert TextData.Successful_order_text in order_title

    @allure.description('Второй заказ самоката с вводом данных. Самокат заказан успешно, отображается номер заказа')
    def test_order_button_on_footer(self, driver):
        order_pages = OrderPages(driver)
        order_pages.click_cookie_button_order()
        order_pages.click_order_button_in_header()
        order_pages.create_order(OrdersData.Order_2)
        order_pages.click_next_button()
        order_pages.input_rental_information(RentalData.Data_2)
        order_pages.wait_for_confirm(OrderPageLocators.Confirm)
        order_pages.click_confirmation_order()
        order_title = order_pages.get_new_order_title(OrderPageLocators.Order_completed)
        order_pages.wait_for_order_completed(OrderPageLocators.Order_completed)
        assert TextData.Successful_order_text in order_title