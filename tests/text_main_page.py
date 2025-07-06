import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from tests.data import ListData, UrlsData
from pages.order_page import OrderPages

@pytest.mark.fixture('driver')
class TestMainPages:
    @pytest.mark.parametrize('index,text', ListData.QuestionsList)
    def test_get_answer_on_question(self, driver, index, text):
        page = BasePage(driver)
        page.open_page(UrlsData.Scooter_url)
        OrderPages(driver).click_cookie_button()
        questions = MainPage(driver)
        questions.scroll_to_questions()
        questions.click_on_question(index)
        answer = questions.get_answer_text()
        questions.wait_for_get_answer()
        assert answer == text