from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class OrderPage(BasePage):
    header = (By.XPATH, '//div[contains(text(), "Для кого самокат")]' )
    name = (By.XPATH, '//input[contains(@placeholder, "Имя")]' )
    last = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]' )
    address = (By.XPATH, '//input[contains(@placeholder, "Адрес: куда привезти заказ")]' )
    metro = (By.XPATH, '//input[contains(@placeholder, "Станция метро")]' )
    phone = (By.XPATH, '//input[contains(@placeholder, "Телефон: на него позвонит курьер")]' )
    next_button = (By.XPATH, '//button[contains(text(), "Далее")]' )

    date = (By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]' )
    date_picker = (By.XPATH, '//div[contains(@class, "react-datepicker__day")]' ) 

    term = (By.XPATH, '//div[contains(@class, "Dropdown-control")]' )
    term_options = (By.XPATH, '//div[contains(@class, "Dropdown-option")]' )

    color_black = (By.ID, "black" )
    color_gray = (By.ID, "grey" )

    comment = (By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]' )

    order_button = (By.XPATH, '//button[contains(text(), "Заказать")]' )
    order_no_button = (By.XPATH, '//button[contains(text(), "Нет")]' )


    form_header = (By.XPATH, '//div[contains(text(), "Хотите оформить заказ?")]' )


    @allure.step("Проверить заголовок")
    def check_header(self):
        el = self.driver.find_element(*self.header)
        return el.is_displayed()
    
    @allure.step("Заполнить форму Для кого самокат")
    def fill_form(self, name, last, address, metro, phone):
        el = self.driver.find_element(*self.name)
        el.send_keys(name)
    
        el = self.driver.find_element(*self.last)
        el.send_keys(last)

        el = self.driver.find_element(*self.address)
        el.send_keys(address)

        el = self.driver.find_element(*self.metro)
        el.click()
        el = self.driver.find_element(By.XPATH, f'//div[contains(text(), "{metro}")]')
        el.click()


        el = self.driver.find_element(*self.phone)
        el.send_keys(phone)

        el = self.driver.find_element(*self.next_button)
        el.click()

    @allure.step("Заполнить форму Аренда")
    def fill_rent_form(self, term_option, color, comment):
        el = self.driver.find_element(*self.date)
        el.click()
    
        el = self.driver.find_elements(*self.date_picker)
        el[-1].click()

        el = self.driver.find_element(*self.term)
        el.click()

        el = self.driver.find_elements(*self.term_options)
        el[term_option].click()

        if color == "grey":
            el = self.driver.find_element(*self.color_gray)
            el.click()

        if color == "black":
            el = self.driver.find_element(*self.color_black)
            el.click()

        el = self.driver.find_element(*self.comment )
        el.send_keys(comment)

        el = self.driver.find_elements(*self.order_button)
        el[1].click()
    

    @allure.step("Проверить заказ")
    def check_order(self):

        el = self.driver.find_element(*self.form_header)
        return el.is_displayed()

    @allure.step("Закрыть заказ")
    def close_order(self):
        el = self.driver.find_element(*self.order_no_button)
        el.click()