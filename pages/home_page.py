from selenium.webdriver.common.by import By

from pages.samokat_page import BasePage, SamokatPage
import allure

from selenium.common.exceptions import NoSuchElementException
import logging

from test_data import HOME_HEADER, QA


class HomePage(SamokatPage):
    question_header = (By.XPATH, '//div[contains(text(), "Вопросы о важном")]' )

    cookie = (By.XPATH, '//button[contains(text(), "да все привыкли")]' )
    order_button_middle = (By.XPATH, '//button[contains( @class, "Button_Middle")]' )
    header = (By.XPATH, '//div[contains( @class, "Home_Header")]' )


    question_cost = (By.XPATH, f'//div[contains(text(), "{QA[0][1]}")]' )
    question_number = (By.XPATH, f'//div[contains(text(), "{QA[1][1]}")]' )
    question_time = (By.XPATH, f'//div[contains(text(), "{QA[2][1]}")]' )
    question_today = (By.XPATH, f'//div[contains(text(), "{QA[3][1]}")]' )
    question_expand = (By.XPATH, f'//div[contains(text(), "{QA[4][1]}")]' )
    question_charge = (By.XPATH, f'//div[contains(text(), "{QA[5][1]}")]' )
    question_cancel = (By.XPATH, f'//div[contains(text(), "{QA[6][1]}")]' )
    question_mkad = (By.XPATH, f'//div[contains(text(), "{QA[7][1]}")]' )

    ans_cost = (By.XPATH, f'//p[contains(text(), "{QA[0][2]}")]' )
    ans_number = (By.XPATH, f'//p[contains(text(), "{QA[1][2]}")]' )
    ans_time = (By.XPATH, f'//p[contains(text(), "{QA[2][2]}")]' )
    ans_today = (By.XPATH, f'//p[contains(text(), "{QA[3][2]}")]' )
    ans_expand = (By.XPATH, f'//p[contains(text(), "{QA[4][2]}")]' )
    ans_charge = (By.XPATH, f'//p[contains(text(), "{QA[5][2]}")]' )
    ans_cancel = (By.XPATH, f'//p[contains(text(), "{QA[6][2]}")]' )
    ans_mkad = (By.XPATH, f'//p[contains(text(), "{QA[7][2]}")]' )



    @allure.step(f"Проверка вопроса {QA[0][1]}")
    def check_question_cost(self):
        return self.check_question(self.question_cost, self.ans_cost)

    @allure.step(f"Проверка вопроса {QA[1][1]}")
    def check_question_number(self):
        return self.check_question(self.question_number, self.ans_number)

    @allure.step(f"Проверка вопроса {QA[2][1]}")
    def check_question_time(self):
        return self.check_question(self.question_time, self.ans_time)

    @allure.step(f"Проверка вопроса {QA[3][1]}")
    def check_question_today(self):
        return self.check_question(self.question_today, self.ans_today)

    @allure.step(f"Проверка вопроса {QA[4][1]}")
    def check_question_expand(self):
        return self.check_question(self.question_expand, self.ans_expand)

    @allure.step(f"Проверка вопроса {QA[5][1]}")
    def check_question_charge(self):
        return self.check_question(self.question_charge, self.ans_charge)

    @allure.step(f"Проверка вопроса {QA[6][1]}")
    def check_question_cancel(self):
        return self.check_question(self.question_cancel, self.ans_cancel)

    @allure.step(f"Проверка вопроса {QA[7][1]}")
    def check_question_mkad(self):
        return self.check_question(self.question_mkad, self.ans_mkad)

    def check_question(self, q, ans):
        qs = self.find(*q)
        
        self.scroll_to_elment(qs)

        qs.click()

        self.wait(ans)

        ans_el = self.find(*ans)
        return ans_el.is_displayed()


    @allure.step("Закрыть куки")
    def close_cookie(self):
        try:
            el = self.find(*self.cookie)
            el.click()
        except NoSuchElementException as e:
            logging.info('Already closed')


    @allure.step("Проверка заголовка Вопросы о важном")
    def check_header(self):
        el = self.find(*self.question_header)
        return el.is_displayed()
    


    @allure.step("Заказать кнопка в середине")
    def order_middle_button(self):
        el = self.find(*self.order_button_middle)
        el.click()

    @allure.step("Проверить заговок")
    def check_home_header(self):
        el = self.find(*self.header)
        return el.text == HOME_HEADER

