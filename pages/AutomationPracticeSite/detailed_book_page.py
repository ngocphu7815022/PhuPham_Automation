from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class DetailedBook(BasePage):
    book_title = (By.TAG_NAME, "h1")
    description_tab = (By.CSS_SELECTOR,"a[href='#tab-description']")
    reviews_tab = (By.CSS_SELECTOR,"a[href='#tab-reviews']")
    description_header = (By.CSS_SELECTOR,"div[id='tab-description'] h2")
    description_context = (By.CSS_SELECTOR,"div[id='tab-description'] p")
    reviews_header = (By.CSS_SELECTOR,"div[id='tab-reviews'] h2")
    reviews_context = (By.CSS_SELECTOR,"div[id='tab-reviews'] p")

    def get_book_title(self):
        return self.find(self.book_title).text
    
    
    def select_description_tab(self):
        self.driver.find_element(*self.description_tab).click()
    
    def check_description_header_visible(self):
        if not self.is_visible(self.description_header):
            return f'{self.description_header} is not displayed'
        
    def check_description_context_visible(self):
        if not self.is_visible(self.description_context):
            return f'{self.description_context} is not displayed'
        
    def get_description_context(self):
        return self.get_text(self.description_context)
        
    def select_reviews_tab(self):
        self.driver.find_element(*self.reviews_tab).click()
    
    def check_reviews_header_visible(self):
        if not self.is_visible(self.reviews_header):
            return f'{self.reviews_header} is not displayed'
        
    def check_reviews_context_visible(self):
        if not self.is_visible(self.reviews_context):
            return f'{self.reviews_context} is not displayed'
        