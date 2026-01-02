from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SecureAreaPage(BasePage):
    message_locator = (By.XPATH, "//div[@id='flash']")

    def get_success_message(self):
        return self.get_text(self.message_locator)
    
    #def get_url(self):
    #   return self.driver.current_url