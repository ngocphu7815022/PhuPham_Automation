from pages.login_page import LoginPage
import pytest
import os 

@pytest.mark.positive
def test_login_success(driver):

    # login 
    login_page = LoginPage(driver)

    login_page.logger.info("===== START test_login_success =====")

    login_page.open_page()
    login_page.login("tomsmith", "SuperSecretPassword!")

    # verify successful message
    actual_message = login_page.get_message()
    expected_message = "You logged into a secure area!"

    assert expected_message in actual_message, f"Expected message to contain '{expected_message}' but got '{actual_message}'"

    # verify URL as expected
    actual_url = driver.current_url
    expected_url = "https://the-internet.herokuapp.com/secure"

    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'"

    login_page.logger.info("===== END test_login_success =====")
    print("CWD =", os.getcwd())


@pytest.mark.negative
def test_login_invalid_username(driver):
    # login 
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("abc", "abc123456")

    # verify failure message
    actual_message = login_page.get_message()
    expected_message = "Your username is invalid!"

    assert expected_message in actual_message, f"Expected message to contain '{expected_message}' but got '{actual_message}'"

    # verify URL as expected
    actual_url = driver.current_url
    expected_url = "https://the-internet.herokuapp.com/login"

    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'"


@pytest.mark.negative
def test_login_invalid_password(driver):
    # login 
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("tomsmith", "abc123456")
    # verify failure message
    actual_message = login_page.get_message()
    expected_message = "Your password is invalid!"

    assert expected_message in actual_message, f"Expected message to contain '{expected_message}' but got '{actual_message}'"

    # verify URL as expected
    actual_url = driver.current_url
    expected_url = "https://the-internet.herokuapp.com/login"

    assert actual_url == expected_url, f"Expected URL to be '{expected_url}' but got '{actual_url}'" 