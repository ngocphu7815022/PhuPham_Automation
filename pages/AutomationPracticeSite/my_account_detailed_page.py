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
    order_summary = (By.XPATH, "//p[mark[contains(@class,'order-number')]]")

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

    def get_view_button_count(self):
        return len(self.finds(self.view_buttons))

    def click_view_button_by_index(self, index):
        locator = (By.XPATH, f"(//a[contains(@class,'view')])[{index}]")
        self.click(locator)

    def _get_order_cell_locator(self, field, child_tag=None):
        xpath = f"//td[contains(@class,'order-{field}')]"
        if child_tag:
            xpath = f"{xpath}//{child_tag}"
        return (By.XPATH, xpath)

    def _get_detail_mark_locator(self, field):
        return (By.XPATH, f"//mark[contains(@class,'order-{field}')]")

    def _get_order_cell_text(self, field, index, child_tag=None):
        locator = self._get_order_cell_locator(field, child_tag)
        return self.finds(locator)[index - 1].text.strip()

    def _click_order_cell(self, field, index, child_tag=None):
        locator = self._get_order_cell_locator(field, child_tag)
        self.finds(locator)[index - 1].click()

    def _get_detail_text(self, field):
        return self.get_text(self._get_detail_mark_locator(field)).strip()

    def _normalize_order_id(self, order_id):
        order_id = order_id.strip()
        if not order_id.startswith("#"):
            return f"#{order_id}"
        return order_id

    def get_order_id_count(self):
        return len(self.finds(self._get_order_cell_locator("number", "a")))

    def get_order_id(self, index):
        return self._normalize_order_id(self._get_order_cell_text("number", index, "a"))

    def get_status(self, index):
        return self._get_order_cell_text("status", index)

    def click_order_id(self, index):
        self._click_order_cell("number", index, "a")

    def get_date(self, index=None):
        if index is None:
            return self._get_detail_text("date")

        return self._get_order_cell_text("date", index, "time")

    def get_detail_order_id(self):
        return self._normalize_order_id(self._get_detail_text("number"))

    def get_detail_status(self):
        return self._get_detail_text("status")

    def get_order_summary(self):
        return self.get_text(self.order_summary).strip()

    def is_order_details_visible(self):
        return self.is_visible(self.lbl_order_details)

    def is_customer_details_visible(self):
        return self.is_visible(self.lbl_customer_details)

    def is_billing_address_visible(self):
        return self.is_visible(self.lbl_billing_address)
