import pytest
from pages.welcome_page import WelcomePage
from pages.flights_page import FlightsPage
from utils.common_assert import assert_equal


def test_booking(driver):
    welcome_page = WelcomePage(driver)

    # Step 1:Open link
    welcome_page.open("https://blazedemo.com/")

    # Step 2: Select departure Portland
    welcome_page.select_departure("Portland")

    # Step 3: Select destination London
    welcome_page.select_destination("London")

    ####
    # Verify that selecting departure, destination is successful
    ####

    # Departure
    selected_departure = welcome_page.get_departure_selected_text()
    expected_departure = "Portland"
    assert_equal(selected_departure, expected_departure, "Departure")

    # Destination
    selected_destination = welcome_page.get_destination_selected_text()
    expected_destination = "London"
    assert_equal(selected_destination, expected_destination, "Destination")

    # Step 4: Click on 'Find Flights' button
    flights_page = welcome_page.select_find_flights()

    ####
    # Verify that moving to next page is successful.
    # Verify that the route text is correctly
    # Verify that the route has the flights
    ####
    flights_page.is_header_displayed()
    actual_header = flights_page.get_header()
    expected_header = f"Flights from {selected_departure} to {selected_destination}:"

    # Check route text
    assert_equal(actual_header, expected_header, "Flights Page header")

    # Step 5: Find how many flights displayed
    flights_count = flights_page.get_flights_count()
    assert flights_count > 0, "No flights found"

    # Step 6: Click on choose this flight button (2nd button).
    detailed_flights = flights_page.select_second_button()

    ####
    # Verify that moving to next page is successful.
    # Verify that the detailed flights header is displayed correctly
    ####
    detailed_flights.is_header_displayed()
    actual_detailed_header = detailed_flights.get_header()
    expected_detailed_header = "Your flight from TLV to SFO has been reserved."

    # Check detailed booking text
    assert_equal(
        actual_detailed_header, expected_detailed_header, "Detailed Booking header"
    )

    # Step 7: Verify the detailed belows displayed
    fields_to_verify = {
        "airline": ("Airline: United", detailed_flights.get_airline),
        "flight_number": ("Flight Number: UA954", detailed_flights.get_flight_number),
        "price": ("Price: 400", detailed_flights.get_price),
        "fees_taxes": (
            "Arbitrary Fees and Taxes: 514.76",
            detailed_flights.get_fees_taxes,
        ),
        "total_cost": ("Total Cost: 914.76", detailed_flights.get_total_cost),
    }

    actual_values = {}

    for field, (expected, getter) in fields_to_verify.items():
        actual = getter()
        actual_values[field] = actual

        assert (
            actual == expected
        ), f"[{field}] Expected '{expected}', but got '{actual}'"

    # Toal cost = price + fees_taxes
    price_number = detailed_flights.extract_float(detailed_flights.get_price())
    fees_taxes_number = detailed_flights.extract_float(
        detailed_flights.get_fees_taxes()
    )
    total = price_number + fees_taxes_number
    total_cost_number = detailed_flights.extract_float(
        detailed_flights.get_total_cost()
    )
    assert (
        total == total_cost_number
    ), f"Expected cost is {total}', but got {total_cost_number}"

    # Step 8: Provide all detailed information
    detailed_flights.enter_detailed_information(
        "Phu",
        "423 Truong Chinh",
        "TPHCM",
        "Tan Binh",
        "700000",
        "233467346",
        1,
        2027,
        "PHAM NGOC PHU",
    )
    detailed_flights.select_card_type("amex")
    detailed_flights.check_remember_me_checkbox()

    # Click on 'Purchase Flight' button
    detailed_purchase = detailed_flights.select_purchase_flight()

    ####
    # Verify that moving to next page is successful.
    # Verify that the detailed flights header is displayed correctly
    ####
    detailed_purchase.is_header_displayed()
    actual_detailed_purchase_header = detailed_purchase.get_header()
    expected_detailed_purchase_header = "Thank you for your purchase today!"

    # Check detailed booking text
    assert_equal(
        actual_detailed_purchase_header,
        expected_detailed_purchase_header,
        "Purchase Page Header",
    )

    # Step 9: Verify details in the Purchase Page
    # Get actual data from the table
    actual_data_table = detailed_purchase.get_table_data()

    expected_data_table = {
        "Id": "1616482160957",
        "Status": "Pending Capture",
        "Amount": "555 USD",
        "Card Number": "xxxxxxxxxxxx1111",
        "Expiration": "11 /2018",
        "Auth Code": "888888",
        "Date": "Tue, 23 Mar 2021 06:49:20 +0000",
    }
    detailed_purchase.verify_table_data(actual_data_table, expected_data_table)
