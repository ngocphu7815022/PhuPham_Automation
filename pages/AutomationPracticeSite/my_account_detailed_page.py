from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MyAccountDetailedPage(BasePage):
    span_hello = (By.XPATH,"//p[contains(text(),'Hello')]")

    def get_hello_text(self):
        self.get_text(self.span_hello)

    def get_email_to_username(self, email):
        return email.split('@')[0]