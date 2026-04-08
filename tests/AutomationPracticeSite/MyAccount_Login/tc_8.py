import pytest
from pages.AutomationPracticeSite.login_page import LoginPage
import allure


@pytest.mark.parametrize(
    "username, password",
    [("abc7815022@gmail.com", "Phuthoidai1.")],
)
def test_login_with_valid_inputs(driver, username, password):
    expected_login_path = "/my-account/"

    login_page = LoginPage(driver)
    login_page.open_home_page()
    login_page.select_my_account()

    with allure.step(f"Login with valid username and password"):
        my_account_detailed_page = login_page.login(username, password)

        actual_hello_text = my_account_detailed_page.get_hello_text()
        expected_username = my_account_detailed_page.get_email_to_username(username)

        assert (
            expected_username in actual_hello_text
        ), f"Expected username '{expected_username}' to appear in '{actual_hello_text}'"

    with allure.step(f"Click on Sign Out button"):
        login_page = my_account_detailed_page.select_sign_out()

        assert driver.current_url.endswith(expected_login_path), (
            f"Expected login page URL after sign out to end with '{expected_login_path}', "
            f"but got '{driver.current_url}'"
        )
        assert (
            login_page.is_lbl_login_displayed()
        ), "Login form is not displayed after sign out"

        driver.back()

        assert driver.current_url.endswith(expected_login_path), (
            f"Expected login page URL after browser back to remain ending with '{expected_login_path}', "
            f"but got '{driver.current_url}'"
        )
        assert (
            login_page.is_lbl_login_displayed()
        ), "Browser back returned to a page that is not showing the login form"
