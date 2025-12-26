import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DzenPage(BasePage):
    header = (By.XPATH, '//header[contains( @class, "dzen-layout")]' )

    @allure.step("Проверить заговок дзен")
    def check_home_header(self):
        self.wait(self.header) 
        el = self.find(*self.header)
        return el.is_displayed()
