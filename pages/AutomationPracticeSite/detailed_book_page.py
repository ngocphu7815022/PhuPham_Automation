from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class DetailedBook(BasePage):
    book_title = (By.TAG_NAME, "h1")

    @allure.step("Get book title on detailed page")
    def get_book_title(self):
        return self.find(self.book_title).text
