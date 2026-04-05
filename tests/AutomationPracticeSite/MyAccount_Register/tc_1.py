import pytest
from pages.AutomationPracticeSite.my_account import MyAccountPage
from pages.AutomationPracticeSite.my_account_detailed_page import MyAccountDetailedPage
from utils.common_assert import assert_equal
import allure

@pytest.mark.parametrize(
    "username, password",
    [
        ("abc78150222@gmail.com", "Phuthoidai1.")
    ],
)
def test_resgister_singin(driver, username, password):
   my_account = MyAccountPage(driver)
   my_account.open_home_page()
   my_account.select_my_account()
   my_account.register_account(username, password)


   my_detailed_account = MyAccountDetailedPage(driver)
   #Xử lý email thành username
   username = my_detailed_account.get_email_to_username(username)

   actual_hello = my_detailed_account.get_hello_text()
   assert username in username, f'Mismatch username'
