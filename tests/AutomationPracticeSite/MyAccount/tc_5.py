"""
Test case: View Billing & Shipping address sau khi login.

Steps (map với test case gốc):
    1. Open the browser                                    -> fixture `driver`
    2. Enter URL "http://practice.automationtesting.in/"   -> login_page.open_home_page()
    3. Click on My Account Menu                            -> login_page.select_my_account()
    4. Enter registered username                           -> login_page.login(username, ...)
    5. Enter password                                      -> login_page.login(..., password)
    6. Click on login button                               -> (gộp trong login_page.login)
    7. Verify user successfully login                      -> my_account_detailed_page.is_logged_in()
    8. Click on My Account link → Dashboard                -> my_account_detailed_page.select_my_account_top()
    9. Click on Address link                               -> my_account_detailed_page.select_addresses()
   10. Verify Billing & Shipping address displayed         -> assert is_addresses_billing_displayed()
                                                              assert is_addresses_shipping_displayed()
"""

import pytest
import allure

from pages.AutomationPracticeSite.login_page import LoginPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage


@pytest.mark.parametrize(
    "username, password",
    [("abc7815022@gmail.com", "Phuthoidai1.")],
)
def test_view_billing_and_shipping_address(driver, username, password):
    login_page = LoginPage(driver)

    # Step 1 + 2: Open browser & navigate to URL
    login_page.open_home_page()

    # Step 3: Click on My Account menu
    login_page.select_my_account()

    # Step 4 + 5 + 6: Enter username, password & click Login
    with allure.step("Login with valid username and password"):
        login_page.login(username, password)
        my_account_detailed_page = MyAccountDetailedPage(driver)

    # Step 7: Verify user successfully logged in
    with allure.step("Verify user has logged in successfully"):
        assert my_account_detailed_page.is_logged_in(), (
            "Expected 'Hello ...' greeting to be visible after login, "
            "but it was not. Login may have failed."
        )

    # Step 8: Click on My Account top link → leads to Dashboard
    with allure.step("Click on My Account top link to go to Dashboard"):
        my_account_detailed_page.select_my_account_top()

        expected_dashboard_path = "/my-account/"
        current_url = driver.current_url
        assert current_url.endswith(expected_dashboard_path), (
            f"Expected URL after clicking My Account to end with "
            f"'{expected_dashboard_path}', but got '{current_url}'"
        )

    # Step 9: Click on Address link in sidebar
    with allure.step("Click on Addresses link in sidebar"):
        my_account_detailed_page.select_addresses()

        expected_addresses_path = "/my-account/edit-address/"
        current_url = driver.current_url
        assert current_url.endswith(expected_addresses_path), (
            f"Expected to navigate to addresses page ending with "
            f"'{expected_addresses_path}', but got '{current_url}'"
        )

    # Step 10: Verify Billing & Shipping address are displayed
    with allure.step("Verify both Billing and Shipping address are displayed"):
        assert my_account_detailed_page.is_addresses_billing_displayed(), (
            "Expected 'Billing address' section to be visible on Addresses page, "
            "but it was not."
        )
        assert my_account_detailed_page.is_addresses_shipping_displayed(), (
            "Expected 'Shipping address' section to be visible on Addresses page, "
            "but it was not."
        )

        # Log nội dung 2 địa chỉ ra Allure để dễ kiểm tra trực quan
        billing_text = my_account_detailed_page.get_addresses_billing_text()
        shipping_text = my_account_detailed_page.get_addresses_shipping_text()
        allure.attach(
            billing_text,
            name="Billing address",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            shipping_text,
            name="Shipping address",
            attachment_type=allure.attachment_type.TEXT,
        )
