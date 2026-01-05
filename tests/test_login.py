from pages.login_page import LoginPage
import pytest

""" Test cases for login functionality 
def test_login_fail(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("invalid_user", "invalid_pass")
  
    assert "Your username is invalid!" in login_page.get_error_message()




def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open_page()

    # check button login is enabled
    assert login_page.is_button_login_enable(), "Login button is not enabled"
    
    #login with valid credentials
    login_page.login("tomsmith", "SuperSecretPassword!")

    #Chờ tới khi redriect thành công và success message hiển thị
    assert login_page.is_message_displayed(), "Success message is not displayed"

    #Verify current url
    current_url = driver.current_url
    assert "/secure" in current_url, "Login was not successful"

"""

@pytest.mark.parametrize(
    "username, password, message",
    [
        ("invalid_user", "invalid_password", "Your username is invalid!"),
        ("tomsmith", "a!", "Your password is invalid!"),
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ]
)
def test_login(driver, username,password,message):
    login_page = LoginPage(driver)
    login_page.open_page()
    
    login_page.login(username, password)

    #verify message is displayed
    assert login_page.is_message_displayed(), "Message is not displayed"
    #verify message text
    actual_message = login_page.get_message()
    assert message in actual_message, f"Expected message to contain '{message}' but got '{actual_message}'"


    # verify URL as expected
    actual_url = driver.current_url

    if username == "tomsmith" and password == "SuperSecretPassword!":
        expected_url = "https://the-internet.herokuapp.com/secure"
    else:
        expected_url = "https://the-internet.herokuapp.com/login"


    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'"
