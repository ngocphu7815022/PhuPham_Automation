from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text, clear=True):
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
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
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element.is_enabled()
    
    def wait_until_enabled(self, locator):
        self.wait.until(lambda driver: self.find(locator).is_enabled())

    def wait_until_disabled(self, locator):
        self.wait.until(lambda driver: not self.find(locator).is_enabled())

    def get_attribute(self, locator, attribute_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute_name)

