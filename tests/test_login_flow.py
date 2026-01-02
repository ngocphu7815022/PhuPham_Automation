from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

def test_login_flow(driver):
    # login 
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")

    # verify successful message
    secure_area_page = SecureAreaPage(driver)
    actual_message = secure_area_page.get_success_message()
    expected_message = "You logged into a secure area!"

    assert expected_message in actual_message, f"Expected message to contain '{expected_message}' but got '{actual_message}'"

    # verify URL as expected
    actual_url = driver.current_url
    expected_url = "https://the-internet.herokuapp.com/secure"

    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'"