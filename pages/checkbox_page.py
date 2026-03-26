from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckboxPage(BasePage):
    checkbox1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox2 = (By.XPATH, "(//input[@type='checkbox'])[2]")

    def check_first_checkbox(self):
        if not self.is_selected(self.checkbox1):
            self.click(self.checkbox1)

    def uncheck_second_checkbox(self):
        if self.is_selected(self.checkbox2):
            self.click(self.checkbox2)        