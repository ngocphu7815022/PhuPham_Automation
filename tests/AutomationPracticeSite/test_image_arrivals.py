import pytest
from pages.AutomationPracticeSite.home_page import HomePage
from pages.AutomationPracticeSite.detailed_book_page import DetailedBook
from utils.common_assert import assert_equal


def test_booking(driver):
    home_page = HomePage(driver)

    home_page.open_home_page()
    home_page.select_shop()
    home_page.select_home()
    home_page.get_active_slides_id()
    home_page.get_active_arrivals_id()


def test_click_each_book_navigate_correctly(driver):
    home_page = HomePage(driver)
    detailed_page = DetailedBook(driver)

    home_page.open_home_page()

    total_books = len(home_page.finds(home_page.books))

    for i in range(total_books):
        expected_title = home_page.click_book_by_index(i)
        actual_title = detailed_page.get_book_title()

        assert_equal(expected_title, actual_title, "Title")

        driver.back()
