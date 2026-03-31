from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class HomePage(BasePage):
    url = "http://practice.automationtesting.in/"
    lbtn_Shop = (By.XPATH,"//a[normalize-space()='Shop']")
    ib_Home = (By.XPATH,"//img[@title='Automation Practice Site']")
    btn_Next = (By.ID,"n2-ss-6-arrow-next")
    sld_Slide = (By.CSS_SELECTOR, ".n2-ss-slide")
    arrivals_ele = (By.CSS_SELECTOR,".sub_row_1-0-2 .sub_column")


    @allure.step("Open page")
    def open_home_page(self):
        self.open(self.url)

    @allure.step("Click on Shop menu")
    def select_shop(self):
        self.click(self.lbtn_Shop)

    @allure.step("Click on Home menu")
    def select_home(self):
        self.click(self.ib_Home)    

    @allure.step("Verify home page has 3 sliders only")
    def get_active_slides_id(self):
        slides = self.finds(self.sld_Slide)
        assert len(slides) == 3

    @allure.step("Verify home page has 3 arrivals only")
    def get_active_arrivals_id(self):
        arrivals = self.finds(self.arrivals_ele)
        assert len(arrivals) == 3