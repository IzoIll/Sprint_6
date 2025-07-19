from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_questions(self, locator):
        return self.driver.find_elements(*locator)

    def get_faq(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_the_faq_page_load(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator))

    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_get_answer(self, locator):
        WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(locator))

    def get_main_header_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_confirm(self, locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator))

    def get_station(self, locator):
        return self.driver.find_element(*locator).click()

    def get_color(self, color):
        return self.driver.find_element(*color).click()

    def wait_for_order_completed(self, locator):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator))

    def get_new_order_title(self, locator):
        new_order_text = self.driver.find_element(*locator).text
        return new_order_text

    def scroll_down(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_faq(locator))