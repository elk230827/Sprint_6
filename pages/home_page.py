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


    
    @allure.step("Проверка вопроса q")
    def check_question(self, q, ans):

        q_locator = f'//div[contains( text(), "{q}")]'
        ans_locator = f'//p[contains( text(), "{ans}")]'
        qs = self.find(By.XPATH, q_locator)
        
        self.scroll_to_elment(qs)

        qs.click()

        self.wait( (By.XPATH, ans_locator) )

        ans_el = self.find(By.XPATH, ans_locator)
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

