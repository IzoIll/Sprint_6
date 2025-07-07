from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import MainPageLocators, OrderPageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_my_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(*locator))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def open_page(self, page):
        self.driver.get(page)

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.Questions)

    def get_faq(self):
        return self.driver.find_element(*MainPageLocators.FAQ)

    def wait_for_the_faq_page_load(self):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(MainPageLocators.FAQ))

    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.Answer).text

    def wait_for_get_answer(self):
        WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(MainPageLocators.Answer))

    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.Header_text).text

    def wait_for_confirm(self):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(OrderPageLocators.Confirm))

    def get_station(self):
        return self.driver.find_element(*OrderPageLocators.Station_dropdown).click()

    def get_color(self, color):
        return self.driver.find_element(*color).click()

    def wait_for_order_completed(self):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(OrderPageLocators.Order_completed))

    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.Order_completed).text
        return new_order_text

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 30).until(ec.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 30).until(ec.url_to_be(url))