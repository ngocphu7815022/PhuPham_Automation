import pytest
from pages.login_error_page import LoginErrorPage  
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("invalid_user", "invalid_password", "Your username is invalid!"),
        ("tomsmith", "invalid_password", "Your password is invalid!"),
    ]
)
def test_login_failed_flow(driver,username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    
    login_page.login(username, password)
    login_error_page = LoginErrorPage(driver)


    #verify error message is displayed
    assert login_error_page.is_error_message_displayed(), "Error message is not displayed"
    #verify error message text
    assert expected_message in login_error_page.get_error_message(), f"Expected error message to contain '{expected_message}' but got '{actual_error_message}'"


    # verify URL as expected
    actual_url = driver.current_url
    expected_url = "https://the-internet.herokuapp.com/login"

    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'"

   