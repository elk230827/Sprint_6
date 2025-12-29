import allure
from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скроллимся к {locator}")
    def scroll_to_elment(self, locator):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(locator).perform()

    def find(self, type, locator):
        return self.driver.find_element(type,locator)

    def find_all(self, type, locator):
        return self.driver.find_elements(type,locator)


    def wait(self, locator):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_any_elements_located(locator) )

    def swtich_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        if len(self.driver.window_handles) > 1:
            
            for window_handle in self.driver.window_handles:
                if window_handle != self.driver.current_window_handle:
                    self. driver.switch_to.window(window_handle)
                    break