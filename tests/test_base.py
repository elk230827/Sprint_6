import pytest
from selenium import webdriver

import config
from pages.home_page import HomePage

class BaseTest:
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 

    @pytest.fixture
    def home_page(self):
        self.driver.get(config.URL)
        
        home_page = HomePage(self.driver)

        home_page.close_cookie()

        return home_page
