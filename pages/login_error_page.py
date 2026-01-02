from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginErrorPage(BasePage):
    error_message_locator = (By.XPATH, "//div[@id='flash']")

    def is_error_message_displayed(self):
        return self.is_visible(self.error_message_locator)

    def get_error_message(self):
        return self.get_text(self.error_message_locator)
    
    