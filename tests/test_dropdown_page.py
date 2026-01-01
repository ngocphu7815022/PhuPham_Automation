from pages.dropdown_page import DropdownPage

def test_dropdown_page(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open("https://the-internet.herokuapp.com/dropdown")
    dropdown_page.select_by_text("Option 1")
    dropdown_page.select_by_value("2")
    dropdown_page.select_by_index(1)
    print(dropdown_page.get_selected_text())
