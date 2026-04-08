from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MyAccountDetailedPage(BasePage):
    span_hello = (By.XPATH, "//p[contains(text(),'Hello')]")
    lbtn_SignOut = (By.XPATH, "//a[normalize-space()='Sign out']")
    lbtn_Dashboard = (By.XPATH, "//a[normalize-space()='Dashboard']")
    lbtn_Orders = (By.XPATH, "//a[normalize-space()='Orders']")

    def get_hello_text(self):
        return self.get_text(self.span_hello)

    def get_email_to_username(self, email):
        return email.split("@")[0]

    def select_sign_out(self):
        from pages.AutomationPracticeSite.login_page import LoginPage

        self.click(self.lbtn_SignOut)
        return LoginPage(self.driver)

    def select_dashboard(self):
        self.click(self.lbtn_Dashboard)
