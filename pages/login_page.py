from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_input = (By.ID,'username')
    password_input = (By.ID,'password')
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    
    def enter_username(self, value):
        self.send_keys(self.username_input, value)

    def enter_password(self, value):
        self.send_keys(self.password_input, value)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()



