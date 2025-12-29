import allure
import pytest

import config
from pages.home_page import HomePage
from test_data import QA
from tests.test_base import BaseTest


class TestQuestions(BaseTest):

    @allure.title("Проверка Вопросы о важном")
    def test_question_header(self, home_page):
        assert home_page.check_header()

    @pytest.mark.parametrize("idx,q,a", QA )
    @allure.title(f"Проверка вопрос {QA[0][1]}")
    def test_question(self, home_page, idx, q, a):
        assert home_page.check_question(q,a)

