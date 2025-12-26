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

    @allure.title(f"Проверка вопрос {QA[0][1]}")
    def test_question_cost(self, home_page):
        assert home_page.check_question_cost()

    @allure.title(f"Проверка вопрос {QA[1][1]}")
    def test_question_number(self, home_page):
        assert home_page.check_question_number()

    @allure.title(f"Проверка вопрос {QA[2][1]}")
    def test_question_time(self, home_page):
        assert home_page.check_question_time()

    @allure.title(f"Проверка вопрос {QA[3][1]}")
    def test_question_today(self, home_page):
        assert home_page.check_question_today()

    @allure.title(f"Проверка вопрос {QA[4][1]}")
    def test_question_expand(self, home_page):
        assert home_page.check_question_expand()

    @allure.title(f"Проверка вопрос {QA[5][1]}")
    def test_charge(self, home_page):
        assert home_page.check_question_charge()

    @allure.title(f"Проверка вопрос {QA[6][1]}")
    def test_question_cancel(self, home_page):
        assert home_page.check_question_cancel()

    @allure.title(f"Проверка вопрос {QA[7][1]}")
    def test_question_mkad(self, home_page):
        assert home_page.check_question_mkad()
