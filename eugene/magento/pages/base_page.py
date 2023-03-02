from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.page_url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def check_url_is(self, url):
        return self.driver.current_url == url
