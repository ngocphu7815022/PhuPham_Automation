from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MyAccountDetailedPage(BasePage):
    span_hello = (By.XPATH, "//p[contains(text(),'Hello')]")
    lbtn_SignOut = (By.XPATH, "//a[normalize-space()='Sign out']")
    lbtn_Dashboard = (By.XPATH, "//a[normalize-space()='Dashboard']")
    lbtn_Orders = (By.XPATH, "//a[normalize-space()='Orders']")
    tbl_Orders = (
        By.XPATH,
        "//table[@class='woocommerce-MyAccount-orders shop_table shop_table_responsive my_account_orders account-orders-table']",
    )
    lbl_empty_order = (
        By.XPATH,
        "//div[@class='woocommerce-Message woocommerce-Message--info woocommerce-info']",
    )
    order_rows = (By.XPATH, "//tr[@class='order']")
    view_buttons = (By.XPATH, "//a[contains(@class,'view')]")
    lbl_order_details = (By.XPATH, "//h2[normalize-space()='Order Details']")
    lbl_customer_details = (By.XPATH, "//h2[normalize-space()='Customer Details']")
    lbl_billing_address = (By.XPATH, "//h3[normalize-space()='Billing Address']")

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

    """
    def click_all_view_buttons(self):
        buttons = self.finds(self.view_buttons)
        total = len(buttons)

        for i in range(total):
            locator = (By.XPATH, f"(//a[contains(@class,'view')])[{i+1}]")
            self.find(locator).click()

            # nếu có navigate thì nên quay lại
            #self.driver.back()
    """

    def get_view_button_count(self):
        return len(self.finds(self.view_buttons))

    def click_view_button_by_index(self, index):
        locator = (By.XPATH, f"(//a[contains(@class,'view')])[{index}]")
        self.click(locator)

    def is_order_details_visible(self):
        return self.is_visible(self.lbl_order_details)

    def is_customer_details_visible(self):
        return self.is_visible(self.lbl_customer_details)

    def is_billing_address_visible(self):
        return self.is_visible(self.lbl_billing_address)
