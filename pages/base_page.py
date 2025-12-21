import allure
from selenium import webdriver

from locators.base_page_locators import LOGO, ORDER_BUTTON_HEADER

class BasePage():
    order_button_header = ORDER_BUTTON_HEADER
    logo = LOGO

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заказать кнопка в хидере")
    def order_header_button(self):
        el = self.driver.find_element(*self.order_button_header)
        el.click()

    @allure.step("Кликнуть лого")
    def click_logo(self):
        el = self.driver.find_element(*self.logo)
        el.click()
