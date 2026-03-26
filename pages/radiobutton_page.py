from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RadioButtonPage(BasePage):
    radio_button_yes = (By.CSS_SELECTOR, "label[for='yesRadio']")
    radio_button_impressive = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    result_text = (By.XPATH, "//p[@class='mt-3']")

    def select_yes(self):
        self.click(self.radio_button_yes)
        return self.get_text(self.result_text)

    def select_impressive(self):
        self.click(self.radio_button_impressive)       
        return self.get_text(self.result_text)
