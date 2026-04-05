from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
from selenium.webdriver.support import expected_conditions as EC
import allure


class MyAccountPage(BasePage):
    url = "http://practice.automationtesting.in/"
    lbtn_MyAccount = (By.XPATH, "//a[normalize-space()='My Account']")
    tb_reg_email = (By.XPATH, "//input[@id='reg_email']")
    tb_reg_password = (By.XPATH, "//input[@id='reg_password']")
    btn_reg = (By.XPATH, "//input[@name='register']")
    tb_email = (By.XPATH,"//input[@id='username']")
    tb_password = (By.XPATH,"//input[@id='password']")
    btn_login = (By.XPATH, "//input[@name='login']")



    def open_home_page(self):
        self.open(self.url)

    def select_my_account(self):
        self.click(self.lbtn_MyAccount)    

    def register_account(self, username, password):
        self.type(self.tb_reg_email, username)
        self.type(self.tb_reg_password, password)
        self.click(self.btn_reg)
     # WAIT cho page mới load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Hello')]"))
        )
        return MyAccountDetailedPage(self.driver)
    