import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def click_cookie_button(self):
        self.click_to_element(*MainPageLocators.Cookie_button)

    @allure.step('Пролистать до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(MainPageLocators.FAQ))

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.Questions)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        questions = self.get_questions()
        questions[index - 1].click()

    @allure.step('Получить текст ответа')
    def get_answer_text(self):
        return self.driver.find_element(*MainPageLocators.Answer).text

    def wait_for_get_answer(self):
        WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(MainPageLocators.Answer))

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.Scooter_logo)

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.Yandex_logo)

    @allure.step('Получить текст заголовка главной страницы')
    def get_main_header_text(self):
        return self.driver.find_element(*MainPageLocators.Header_text).text