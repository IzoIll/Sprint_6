import allure
from locators.locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Кликнуть на кнопку "да все привыкли"')
    def click_cookie_button(self):
        self.click_to_element(*MainPageLocators.Cookie_button)

    @allure.step('Пролистать до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", BasePage.get_faq(self))
        BasePage.wait_for_the_faq_page_load(self)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, index):
        questions = self.get_questions()
        questions[index - 1].click()

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.Scooter_logo)

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.Yandex_logo)