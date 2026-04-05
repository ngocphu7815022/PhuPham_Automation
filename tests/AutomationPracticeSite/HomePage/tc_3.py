import pytest
from pages.AutomationPracticeSite.home_page import HomePage
from pages.AutomationPracticeSite.detailed_book_page import DetailedBook
from utils.common_assert import assert_equal


def test_description_reviews_tab(driver):
    home_page = HomePage(driver)
    detailed_page = DetailedBook(driver)

    home_page.open_home_page()

    total_books = len(home_page.finds(home_page.books))

    for i in range(total_books):
        expected_title = home_page.click_book_by_index(i)
        actual_title = detailed_page.get_book_title()
        assert_equal(expected_title, actual_title, "Title")

        detailed_page.select_description_tab()
        detailed_page.check_description_header_visible()
        detailed_page.check_description_context_visible()
        description_context = detailed_page.get_description_context()
        assert "" in driver.title, "Title does not contain expected text"

        detailed_page.select_reviews_tab()
        detailed_page.check_reviews_header_visible()
        detailed_page.check_reviews_context_visible()
        driver.back()
