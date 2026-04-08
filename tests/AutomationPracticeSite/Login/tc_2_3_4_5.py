import pytest
from pages.AutomationPracticeSite.login_page import LoginPage
import allure


# MY ACCOUNT-LOGIN - Test cases 2, 3, 4, 5
@pytest.mark.parametrize(
    "scenario, username, password, error_message",
    [
        (
            "Wrong username and password",
            "phuphamlaidon@gmail.com",
            "Phuthoidai1.",
            "Error: A user could not be found with this email address.",
        ),
        (
            "Correct username and empty password",
            "abc7815022@gmail.com",
            "",
            "Error: Password is required.",
        ),
        (
            "Empty username and valid password",
            "",
            "Phuthoidai1.",
            "Error: Username is required.",
        ),
        ("Empty username and empty password", "", "", "Error: Username is required."),
    ],
    ids=lambda x: x if isinstance(x, str) else None,
)
def test_login_with_invalid_inputs(driver, scenario, username, password, error_message):
    with allure.step(f"Scenario: {scenario}"):
        login_page = LoginPage(driver)
        login_page.open_home_page()
        login_page.select_my_account()
        login_page.login(username, password)

        actual_error_message = login_page.get_error_message()

        assert (
            error_message in actual_error_message
        ), f"[{scenario}] Expected '{error_message}' but got '{actual_error_message}'"


# MY ACCOUNT-LOGIN - Test cases 7
@pytest.mark.parametrize(
    "scenario, username, password, error_message",
    [
        (
            "Valid username and password with casing (Case-sensitivity check)",
            "ABC7815022",
            "PHUTHOIDAI1.",
            "Error: The password you entered for the username {username} is incorrect. Lost your password?",
        ),
        (
            "Valid username and password with casing (Case-sensitivity check)",
            "abc7815022",
            "PHUTHOIDAI1.",
            "Error: The password you entered for the username {username} is incorrect. Lost your password?",
        ),
    ],
    ids=lambda x: x if isinstance(x, str) else None,
)
def test_login_with_casing(driver, scenario, username, password, error_message):
    with allure.step(f"Scenario: {scenario}"):
        login_page = LoginPage(driver)
        login_page.open_home_page()
        login_page.select_my_account()
        login_page.login(username, password)

        actual_error_message = login_page.get_error_message()
        expected_error_message = error_message.format(username=username)

        assert (
            expected_error_message in actual_error_message
        ), f"[{scenario}] Expected '{expected_error_message}' but got '{actual_error_message}'"
