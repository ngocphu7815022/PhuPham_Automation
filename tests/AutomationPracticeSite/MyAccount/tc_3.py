import pytest
from pages.AutomationPracticeSite.login_page import LoginPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
import allure


@pytest.mark.parametrize(
    "username, password, has_orders",
    [
        ("abc7815022@gmail.com", "Phuthoidai1.", True),
    ],
)
def test_orders_menu(driver, username, password, has_orders):
    login_page = LoginPage(driver)
    login_page.open_home_page()
    login_page.select_my_account()

    with allure.step(f"Login with valid username and password"):
        expected_login_path = "/my-account/orders/"

        login_page.login(username, password)
        my_account_detailed_page = MyAccountDetailedPage(driver)

    with allure.step(f"Select Orders"):
        my_account_detailed_page.select_orders()
        current_url = driver.current_url
        assert current_url.endswith(expected_login_path), (
            f"Expected login page URL after browser back to remain ending with '{expected_login_path}', "
            f"but got '{current_url}'"
        )

    with allure.step("Verify Orders content matches expected account state"):
        is_empty_message_displayed = (
            my_account_detailed_page.is_no_order_message_displayed()
        )
        is_order_table_displayed = my_account_detailed_page.is_order_table_displayed()

        if has_orders:
            assert is_order_table_displayed, "Expected orders table to be displayed."
            assert (
                my_account_detailed_page.get_order_count() > 0
            ), "Expected at least one order row to be displayed."
            assert (
                not is_empty_message_displayed
            ), "Did not expect the empty order message for an account with orders."
        else:
            assert (
                is_empty_message_displayed
            ), "Expected the empty order message to be displayed."
            assert (
                not is_order_table_displayed
            ), "Did not expect the orders table for an account without orders."

    with allure.step("Click on 'View' button in each row"):
        total_view_buttons = my_account_detailed_page.get_view_button_count()

        for index in range(1, total_view_buttons + 1):
            with allure.step(
                f"Click 'View' button at row {index} and verify related labels"
            ):
                my_account_detailed_page.click_view_button_by_index(index)

                assert my_account_detailed_page.is_order_details_visible(), (
                    f"Expected 'Order Details' label to be displayed after clicking "
                    f"'View' button at row {index}."
                )
                assert my_account_detailed_page.is_customer_details_visible(), (
                    f"Expected 'Customer Details' label to be displayed after clicking "
                    f"'View' button at row {index}."
                )
                assert my_account_detailed_page.is_billing_address_visible(), (
                    f"Expected 'Billing Address' label to be displayed after clicking "
                    f"'View' button at row {index}."
                )

                driver.back()

                current_url = driver.current_url
                assert current_url.endswith(expected_login_path), (
                    f"Expected to return to the orders page ending with "
                    f"'{expected_login_path}', but got '{current_url}'"
                )
