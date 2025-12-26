import allure
import config
from pages.dzen_page import DzenPage
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestView(BaseTest):
    @allure.title("Проверка лого яндекса")
    def test_yandex_logo(self):
        self.driver.get(config.URL)
        
        home_page = HomePage(self.driver)
        home_page.click_yandex_logo()
        home_page.swtich_window()
        
        dzen_page = DzenPage(self.driver)


        assert dzen_page.check_home_header()

