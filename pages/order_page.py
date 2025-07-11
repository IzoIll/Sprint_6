import allure
from selenium.webdriver import Keys
from locators.locators import MainPageLocators, OrderPageLocators
from pages.base_page import BasePage

class OrderPages(BasePage):
    @allure.step('Кликнуть на кнопку "да все привыкли"')
    def click_cookie_button_order(self):
        self.click_to_element(MainPageLocators.Cookie_button)

    @allure.step("Заполняем поле с именем")
    def set_name_to_field(self, name):
        self.set_text_to_element(OrderPageLocators.Name_field_locator, name)

    @allure.step("Заполняем поле с фамилией")
    def set_lastname_to_field(self, lastname):
        self.set_text_to_element(OrderPageLocators.Lastname_field_locator, lastname)

    @allure.step("Заполняем поле с адресом")
    def set_address_to_field(self, address):
        self.set_text_to_element(OrderPageLocators.Address_field, address)

    @allure.step("Заполняем поле с метро")
    def set_station(self, station):
        self.set_text_to_element(OrderPageLocators.Station_field, station)
        self.get_station(OrderPageLocators.Station_dropdown)

    @allure.step("Заполняем поле с телефоном")
    def set_number_to_field(self, number):
        self.set_text_to_element(OrderPageLocators.Phone_number_field, number)

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.click_to_element(OrderPageLocators.Order_button_in_header)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.Next_button)

    @allure.step('Заполняем поля заказа')
    def create_order(self, client):
        self.set_name_to_field(client.get('name'))
        self.set_lastname_to_field(client.get('lastname'))
        self.set_address_to_field(client.get('address'))
        self.set_station(client.get('station'))
        self.set_number_to_field(client.get('number'))

    @allure.step('Заполняем поле "Дата"')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.Date_field, date)
        self.set_text_to_element(OrderPageLocators.Date_field, Keys.ENTER)

    @allure.step('Выбираем дату заказа')
    def select_rental_period(self, period):
        self.click_to_element(OrderPageLocators.Rental_period)
        self.click_to_element(OrderPageLocators.One_day)

    @allure.step("Выбираем самокат чёрного цвета")
    def click_checkbox(self, color):
        self.get_color(color)

    @allure.step('Заполняем поле "Комментарий"')
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.Comment_field, comment)

    @allure.step('Клик по кнопке "Заказ"')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.Order_button)

    @allure.step('Заполнить раздел "Про аренду"')
    def input_rental_information(self, rental_data):
        color_checkbox = {"black": OrderPageLocators.Black_checkbox, "grey": OrderPageLocators.Grey_checkbox}
        day_period = {"one": OrderPageLocators.One_day, "two": OrderPageLocators.Two_day}
        self.set_date(rental_data.get('date'))
        self.select_rental_period(day_period.get(rental_data.get('day')))
        self.click_checkbox(color_checkbox.get(rental_data.get('color')))
        self.set_comment(rental_data.get('comment'))
        self.click_order_button()

    @allure.step('Клик по кнопке "Да" в диалоге подтверждения')
    def click_confirmation_order(self):
        self.click_to_element(OrderPageLocators.Yes_button)