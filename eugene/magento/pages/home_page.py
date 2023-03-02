from pages.base_page import BasePage
from pages.locators import home_page_locators as loc


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://magento.softwaretestingboard.com/'

    @property
    def search_field(self):
        return self.find(loc.search_field_locator)

    def search_is_displayed(self):
        # search_field = self.driver.find_element(*search_field_locator)
        # search_field = self.find(loc.search_field_locator)
        search_field = self.search_field
        return search_field.is_displayed()

    def execute_search(self, text):
        # search_field = self.find(loc.search_field_locator)
        search_field = self.search_field
        search_field.send_keys(text)
        search_field.submit()
