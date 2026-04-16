from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MyAccountDetailedPage(BasePage):
    span_hello = (By.XPATH, "//p[contains(text(),'Hello')]")
    lbtn_SignOut = (By.XPATH, "//a[normalize-space()='Sign out']")
    lbtn_Dashboard = (By.XPATH, "//a[normalize-space()='Dashboard']")
    lbtn_Orders = (By.XPATH, "//a[normalize-space()='Orders']")
    tbl_Orders = (By.XPATH,"//table[@class='woocommerce-MyAccount-orders shop_table shop_table_responsive my_account_orders account-orders-table']")
    lbl_empty_order = (By.XPATH,"//div[@class='woocommerce-Message woocommerce-Message--info woocommerce-info']")
    order_rows = (By.XPATH,"//tr[@class='order']")

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

    def select_orders(self):
        self.click(self.lbtn_Orders)

    def is_order_table_displayed(self):
        return self.is_visible(self.tbl_Orders)

    def get_order_count(self):
        return len(self.driver.find_elements(*self.order_rows))

    def is_no_order_message_displayed(self):
        return self.is_visible(self.lbl_empty_order)