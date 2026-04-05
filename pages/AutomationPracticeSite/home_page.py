from pages.base_page import BasePage
from pages.AutomationPracticeSite.detailed_book_page import DetailedBook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):
    url = "http://practice.automationtesting.in/"
    lbtn_Shop = (By.XPATH, "//a[normalize-space()='Shop']")
    ib_Home = (By.XPATH, "//img[@title='Automation Practice Site']")
    btn_Next = (By.ID, "n2-ss-6-arrow-next")
    sld_Slide = (By.CSS_SELECTOR, ".n2-ss-slide")
    arrivals_ele = (By.CSS_SELECTOR, ".sub_row_1-0-2 .sub_column")
    books = (By.CSS_SELECTOR, ".sub_row_1-0-2 .sub_column_post_22")
    books_title = (By.XPATH, ".//h3")
    books_img = (By.XPATH, ".//img")
    books_price = (By.XPATH, ".//span")

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

    def get_arrival_books(self):
        return self.finds(self.books)

    def click_book_by_index(self, index):
        items = self.get_arrival_books()
        item = items[index]

        title = item.find_element(*self.books_title).text
        item.find_element(*self.books_img).click()

        return title

    """
    @allure.step("Click on book {title} to navigate to next page")
    def click_on_book_img(self):    
        items = self.get_arrival_books()
        for i in range(len(items)):

             # ⚠️ Re-find lại element mỗi vòng (tránh stale element)
            items = self.get_arrival_books()
            item = items[i]

            title = item.find_element(*self.books_title).text

            # Click
            self.click_book_by_index(i)

            # Wait sang detail page
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )

            # Quay lại trang home
            self.driver.back()

            # Wait lại list load lại
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.books)
            )
    """
