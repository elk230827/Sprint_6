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

