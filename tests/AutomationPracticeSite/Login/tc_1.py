import pytest
from pages.AutomationPracticeSite.login_page import LoginPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
import allure


@pytest.mark.parametrize(
    "username, password",
    [("abc7815022@gmail.com", "Phuthoidai1.")],
    [("abc7815022", "Phuthoidai1.")],
)
def test_login_with_valid_inputs(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_home_page()
    login_page.select_my_account()

    with allure.step(f"Check password is maked or not?"):
        assert login_page.is_password_masked(), "Password field is not masked"

    with allure.step(f"Login with valid username and password"):
        login_page.login(username, password)
        my_account_detailed_page = MyAccountDetailedPage(driver)

        actual_hello_text = my_account_detailed_page.get_hello_text()
        expected_username = my_account_detailed_page.get_email_to_username(username)

        assert (
            expected_username in actual_hello_text
        ), f"Expected username '{expected_username}' to appear in '{actual_hello_text}'"
