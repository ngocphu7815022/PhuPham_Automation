from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "https://the-internet.herokuapp.com/login"

    username_input = (By.ID,'username')
    password_input = (By.ID,'password')
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    message = (By.ID, 'flash')

    def open_page(self):
        self.logger.info("Opening login page")
        self.open(self.url)

    def login(self, username, password):
        self.logger.info(f"Logging in with username: {username}")
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button) 

    def get_message(self):
        return self.get_text(self.message)
    
    def is_message_displayed(self):
        return self.is_visible(self.message)
    
    def is_button_login_enable(self):
        return self.is_enabled(self.login_button)
    

