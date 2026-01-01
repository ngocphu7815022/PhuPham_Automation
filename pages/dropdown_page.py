from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage(BasePage):
    dropdown_menu = (By.ID, "dropdown")


    def select_by_text(self, text): 
        Select(self.find(self.dropdown_menu)).select_by_visible_text(text)


    def select_by_value(self, value):   
        Select(self.find(self.dropdown_menu)).select_by_value(value)

    
    def select_by_index(self, index):   
        Select(self.find(self.dropdown_menu)).select_by_index(index)
    
    #lấy item đầu tiên làm item được chọn
    def get_selected_text(self):
        select = Select(self.find(self.dropdown_menu))
        return select.first_selected_option.text