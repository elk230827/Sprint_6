from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException

from tests.test_data import HOME_HEADER

class HomePage(BasePage):
    question_header = (By.XPATH, '//div[contains(text(), "Вопросы о важном")]' )
    question_element = (By.CLASS_NAME, 'accordion__heading' ) 
    answers = (By.CLASS_NAME, 'accordion__panel' )
    cookie = (By.XPATH, '//button[contains(text(), "да все привыкли")]' )
    order_button_middle = (By.XPATH, '//button[contains( @class, "Button_Middle")]' )
    header = (By.XPATH, '//div[contains( @class, "Home_Header")]' )


    @allure.step("Закрыть куки")
    def close_cookie(self):
        try:
            el = self.driver.find_element(*self.cookie)
            el.click()
        except NoSuchElementException as e:
            print('Already closed')


    @allure.step("Проверка заголовка Вопросы о важном")
    def check_header(self):
        el = self.driver.find_element(*self.question_header)
        return el.is_displayed()
    
    @allure.step("Проверка вопроса {q}")
    def check_question(self, index, q):
        els = self.driver.find_elements(*self.question_element)
        return els[index].is_displayed() and els[index].text == q   

    @allure.step("Проверка ответа {q}")
    def check_answer(self, index, q, ans):
        qs = self.driver.find_elements(*self.question_element)
        

        actions = ActionChains(self.driver)
        actions.scroll_to_element(qs[index]).perform()

        qs[index].click()

        WebDriverWait(self.driver, 1).until( EC.visibility_of_any_elements_located(self.answers) )

        els = self.driver.find_elements(*self.answers)
        return els[index].text == ans
    

    @allure.step("Заказать кнопка в середине")
    def order_middle_button(self):
        el = self.driver.find_element(*self.order_button_middle)
        el.click()

    @allure.step("Проверить заговок")
    def check_home_header(self):
        el = self.driver.find_element(*self.header)
        return el.text == HOME_HEADER

