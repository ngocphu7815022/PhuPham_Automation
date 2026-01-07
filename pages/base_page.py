from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)



    def open(self, url):
        self.logger.info(f"Open page: {url}")
        self.driver.get(url)

    def find(self, locator):
        self.logger.info(f"Find element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Click element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text, clear=True):
        self.logger.info(f"Type into element: {locator}")
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.logger.info(f"Check visibility of element: {locator}")
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def is_selected(self, locator):
        self.logger.info(f"Check if element is selected: {locator}")
        element = self.find(locator)
        return element.is_selected()

    def get_text(self, locator):
        self.logger.info(f"Get text from element: {locator}")
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
        self.logger.info(f"Get attribute '{attribute_name}' from element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute_name)

