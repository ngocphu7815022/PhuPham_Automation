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

    with allure.step("Click on 'order number' in each row"):
        total_order_ids = my_account_detailed_page.get_order_id_count()

        for index in range(1, total_order_ids + 1):
            with allure.step(
                f"Click order id at row {index} and verify related labels"
            ):
                expected_order_id = my_account_detailed_page.get_order_id(index)
                expected_date = my_account_detailed_page.get_date(index)
                expected_status = my_account_detailed_page.get_status(index)
                my_account_detailed_page.click_order_id(index)

                assert (
                    my_account_detailed_page.get_detail_order_id() == expected_order_id
                ), (
                    f"Expected order id in detail page to be '{expected_order_id}' "
                    f"for row {index}, but got "
                    f"'{my_account_detailed_page.get_detail_order_id()}'."
                )
                assert my_account_detailed_page.get_date() == expected_date, (
                    f"Expected order date in detail page to be '{expected_date}' "
                    f"for row {index}, but got '{my_account_detailed_page.get_date()}'."
                )
                assert (
                    my_account_detailed_page.get_detail_status() == expected_status
                ), (
                    f"Expected order status in detail page to be '{expected_status}' "
                    f"for row {index}, but got "
                    f"'{my_account_detailed_page.get_detail_status()}'."
                )

                order_summary = my_account_detailed_page.get_order_summary()
                assert expected_order_id in order_summary, (
                    f"Expected order summary to contain order id '{expected_order_id}', "
                    f"but got '{order_summary}'."
                )
                assert expected_date in order_summary, (
                    f"Expected order summary to contain date '{expected_date}', "
                    f"but got '{order_summary}'."
                )
                assert expected_status in order_summary, (
                    f"Expected order summary to contain status '{expected_status}', "
                    f"but got '{order_summary}'."
                )

                driver.back()

                current_url = driver.current_url
                assert current_url.endswith(expected_login_path), (
                    f"Expected to return to the orders page ending with "
                    f"'{expected_login_path}', but got '{current_url}'"
                )
