import allure
import config
from pages.base_page import BasePage
from pages.dzen_page import DzenPage
from pages.home_page import HomePage
from pages.samokat_page import SamokatPage
from tests.test_base import BaseTest


class TestView(BaseTest):
    @allure.title("Проверка лого яндекса")
    def test_yandex_logo(self):
        self.driver.get(config.URL)

        page = SamokatPage(self.driver)
        page.click_yandex_logo()
        page.swtich_window()
        
        dzen_page = DzenPage(self.driver)


        assert dzen_page.check_home_header()

