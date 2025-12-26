import allure
import config
from pages.home_page import HomePage
from pages.order_page import OrderPage
from tests.test_base import BaseTest
from test_data import LAST, COMMENT, NAME, ADDRESS, COLOR, METRO, PHONE, TERM_OPTION


class TestOrder(BaseTest):
    @allure.title("Заказ через кнопку на странице")
    def test_order_home_middle(self):
        self.driver.get(config.URL)
        
        home_page = HomePage(self.driver)

        home_page.close_cookie()

        home_page.order_middle_button()

        order_page = OrderPage(self.driver)

        assert order_page.check_header()

    @allure.title("Заказ через кнопку в заговке")
    def test_order_header(self):
        self.driver.get(config.URL)
        
        home_page = HomePage(self.driver)

        home_page.close_cookie()

        home_page.order_header_button()

        order_page = OrderPage(self.driver)

        assert order_page.check_header()

    @allure.title("Проверка процесса заказа")
    def test_order_flow(self):
        self.driver.get(config.URL)
        
        home_page = HomePage(self.driver)

        home_page.close_cookie()

        home_page.order_header_button()

        order_page = OrderPage(self.driver)

        assert order_page.check_header()

        order_page.fill_form(NAME, LAST, ADDRESS, METRO, PHONE)

        order_page.fill_rent_form(TERM_OPTION, COLOR, COMMENT)

        assert order_page.check_order()

        order_page.close_order()

        order_page.click_logo()

        home_page = HomePage(self.driver)

        assert home_page.check_home_header()



