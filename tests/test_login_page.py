from pages.login_page import LoginPage

def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")



