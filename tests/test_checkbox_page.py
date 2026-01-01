from pages.checkbox_page import CheckboxPage

def test_checkbox_page(driver):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open("https://the-internet.herokuapp.com/checkboxes")
    checkbox_page.check_first_checkbox()
    checkbox_page.uncheck_second_checkbox()