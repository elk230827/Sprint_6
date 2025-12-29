import pytest

import config
from pages.home_page import HomePage
from selenium import webdriver


@pytest.fixture
def home_page():
    driver = webdriver.Chrome()
    driver.get(config.URL)
    
    home_page = HomePage(driver)

    home_page.close_cookie()

    return home_page
