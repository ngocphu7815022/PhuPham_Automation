from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def send_keys(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False
        
    def is_selected(self, locator):
        element = self.find(locator)
        return element.is_selected()

    def get_text(self, locator):
        element = self.find(locator)
        return element.text     
    
    def is_enabled(self, locator):
        element = self.find(locator)
        return element.is_enabled()
    
    def wait_until_enabled(self, locator):
        self.wait.until(lambda driver: self.find(locator).is_enabled())

    def wait_until_disabled(self, locator):
        self.wait.until(lambda driver: not self.find(locator).is_enabled())

"""
    def get_all_options(self, locator):
        element = self.find(locator)
        #select = Select(element)
        return select.options
"""