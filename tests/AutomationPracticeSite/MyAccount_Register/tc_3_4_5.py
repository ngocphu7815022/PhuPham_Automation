import pytest
from pages.AutomationPracticeSite.my_account import MyAccountPage
from utils.common_assert import assert_equal
import allure


@pytest.mark.parametrize(
    "username, password, error_message",
    [
        ("", "", "Error: Please provide a valid email address."),
        ("", "Phuthoidai1.", "Error: Please provide a valid email address."),
        ("abc127815022@gmail.com", "", "Error: Please enter an account password."),
    ],
)
def test_login_unhappy_cases(driver, username, password, error_message):
    my_account = MyAccountPage(driver)
    my_account.open_home_page()
    my_account.select_my_account()
    my_account.register_account(username, password)
    my_account.select_register()

    actual_error_message = my_account.get_error_message()
    assert (
        error_message == actual_error_message
    ), f"Expected error message is'{error_message}' but got '{actual_error_message}'"
