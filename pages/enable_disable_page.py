from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class EnableDisablePage(BasePage):
    input_field = (By.XPATH,"//form[@id='input-example']//input[@type='text']")
    enable_button = (By.XPATH,"//button[normalize-space()='Enable']")
    
    def toogle_input(self):
        was_enabled = self.is_enabled(self.input_field)

        self.click(self.enable_button)

        if was_enabled:
            self.wait_until_disabled(self.input_field)
        else:
            self.wait_until_enabled(self.input_field)
        