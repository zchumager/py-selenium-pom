from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.search_text_box = self.driver.find_element_by_id("twotabsearchtextbox")
        self.search_button = self.driver.find_element_by_xpath("//input[@type='submit' and @class='nav-input']")
