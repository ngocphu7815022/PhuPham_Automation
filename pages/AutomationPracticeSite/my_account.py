from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class MyAccountPage(BasePage):
    url = "http://practice.automationtesting.in/"
    lbtn_MyAccount = (By.XPATH, "//a[normalize-space()='My Account']")
    tb_reg_email = (By.XPATH, "//input[@id='reg_email']")
    tb_reg_password = (By.XPATH, "//input[@id='reg_password']")
    btn_reg = (By.XPATH, "//input[@name='register']")
    password_strength = (By.CSS_SELECTOR, ".woocommerce-password-strength")
    tb_email = (By.XPATH, "//input[@id='username']")
    tb_password = (By.XPATH, "//input[@id='password']")
    btn_login = (By.XPATH, "//input[@name='login']")
    error_message = (By.XPATH, "//div[@id='body']//li[1]")

    def open_home_page(self):
        self.open(self.url)

    def select_my_account(self):
        self.click(self.lbtn_MyAccount)

    def get_validation_reg_email(self):
        return self.get_validation_message_with_wait(self.tb_reg_email)

    def wait_for_register_button_ready(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_reg))

    def register_account(self, username, password):
        self.type(self.tb_reg_email, username)
        self.type(self.tb_reg_password, password)

        # WooCommerce validates password strength asynchronously and may keep
        # the Register button disabled for a short time after typing.
        if password:
            self.wait_for_register_button_ready()
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Hello')]"))
        )
        return MyAccountDetailedPage(self.driver)
        """

    def select_register(self):
        self.click(self.btn_reg)

    def get_error_message(self):
        return self.get_text(self.error_message)
