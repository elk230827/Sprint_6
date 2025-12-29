from locators.base_page_locators import LOGO, ORDER_BUTTON_HEADER, YANDEX_LOGO


import allure

from pages.base_page import BasePage


class SamokatPage(BasePage):
    order_button_header = ORDER_BUTTON_HEADER
    logo = LOGO
    yandex_logo = YANDEX_LOGO


    @allure.step("Заказать кнопка в хидере")
    def order_header_button(self):
        el = self.find(*self.order_button_header)
        el.click()

    @allure.step("Кликнуть лого яндекса")
    def click_yandex_logo(self):
        el = self.find(*self.yandex_logo)
        el.click()


    @allure.step("Кликнуть лого")
    def click_logo(self):
        el = self.find(*self.logo)
        el.click()


