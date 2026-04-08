from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class LoginPage(BasePage):
    url = "http://practice.automationtesting.in/"
    lbtn_MyAccount = (By.XPATH, "//a[normalize-space()='My Account']")
    tb_email = (By.XPATH, "//input[@id='username']")
    tb_password = (By.XPATH, "//input[@id='password']")
    btn_login = (By.XPATH, "//input[@name='login']")
    error_message = (By.XPATH, "//div[@id='body']//li[1]")
    lbl_login = (By.XPATH, "//h2[normalize-space()='Login']")

    @allure.step("Open Automation Practice Site home page")
    def open_home_page(self):
        self.open(self.url)

    @allure.step("Open My Account page")
    def select_my_account(self):
        self.click(self.lbtn_MyAccount)

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        from pages.AutomationPracticeSite.my_account_detailed_page import (
            MyAccountDetailedPage,
        )

        self.type(self.tb_email, username)
        self.type(self.tb_password, password)
        self.click(self.btn_login)
        return MyAccountDetailedPage(self.driver)

    @allure.step("Click Login button")
    def select_login(self):
        self.click(self.btn_login)

    @allure.step("Get login error message")
    def get_error_message(self):
        return self.get_text(self.error_message)

    @allure.step("Check login button is enabled")
    def is_button_login_enable(self):
        return self.is_enabled(self.btn_login)

    def is_password_masked(self):
        return self.find(self.tb_password).get_attribute("type") == "password"

    def is_lbl_login_displayed(self):
        return self.is_visible(self.lbl_login)
