import pytest
from pages.AutomationPracticeSite.login_page import LoginPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
import allure


@pytest.mark.parametrize(
    "username, password",
    [("abc7815022@gmail.com", "Phuthoidai1.")],
)
def test_select_left_menu(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_home_page()
    login_page.select_my_account()

    with allure.step(f"Login with valid username and password"):
        expected_login_path = "/my-account/"

        login_page.login(username, password)
        my_account_detailed_page = MyAccountDetailedPage(driver)

    with allure.step(f"Select Dashboard"):
        my_account_detailed_page.select_dashboard()
        current_url = driver.current_url
        assert current_url.endswith(expected_login_path), (
            f"Expected login page URL after browser back to remain ending with '{expected_login_path}', "
            f"but got '{current_url}'"
        )
