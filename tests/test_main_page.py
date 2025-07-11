import allure
import pytest
from pages.main_page import MainPage
from Data.data import ListData
from locators.locators import MainPageLocators

@pytest.mark.fixture('driver')
class TestMainPages:
    @allure.title('Проверка выпадающего списка "Разговоры о важном" на соответствие')
    @allure.description('Нажать на выпадающий список. Текст вопросов и ответов соответствует заявленному')
    @pytest.mark.parametrize('index, text', ListData.QuestionsList)
    def test_get_answer_on_question(self, driver, index, text):
        questions = MainPage(driver)
        questions.click_cookie_button_main()
        questions.scroll_to_questions()
        questions.click_on_question(index)
        answer = questions.get_answer_text(MainPageLocators.Answer)
        questions.wait_for_get_answer(MainPageLocators.Answer)
        assert answer == text