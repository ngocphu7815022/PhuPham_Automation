import pytest
from pages.AutomationPracticeSite.home_page import HomePage
from utils.common_assert import assert_equal


def test_booking(driver):
    home_page = HomePage(driver)

    home_page.open_home_page()
    home_page.select_shop()
    home_page.select_home()
    home_page.get_active_slides_id()
    home_page.get_active_arrivals_id()
