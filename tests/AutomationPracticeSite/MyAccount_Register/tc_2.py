import pytest
from pages.AutomationPracticeSite.my_account import MyAccountPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
from utils.common_assert import assert_equal
import allure


@pytest.mark.parametrize(
    "username, password",
    [("abc", "Phuthoidai1.")],
)
def test_invalid_email_format(driver, username, password):
    my_account = MyAccountPage(driver)
    my_account.open_home_page()
    my_account.select_my_account()
    my_account.register_account(username, password)
    my_account.select_register()

    expected_warning = my_account.get_validation_reg_email()
    assert "Please include an '@'" in expected_warning
