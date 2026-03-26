import pytest
from pages.welcome_page import WelcomePage
from pages.flights_page import FlightsPage


def test_booking(driver):
    welcome_page = WelcomePage(driver)
    #Step 1:Open link
    welcome_page.open("https://blazedemo.com/")

    #Step 2: Select departure Portland
    welcome_page.select_departure('Portland')

    #Step 3: Select destination London
    welcome_page.select_destination('London')

    ####
        #Verify that selecting departure, destination is successful
    ####
    selected_departure = welcome_page.get_departure_selected_text()
    assert selected_departure == 'Portland', f"Expected text is Portland, but got '{selected_departure}'"
    selected_destination = welcome_page.get_destination_selected_text()
    assert selected_destination == 'London', f"Expected text is London, but got '{selected_destination}'"

    #Step 4: Click on 'Find Flights' button
    flights_page = welcome_page.select_find_flights()

    ####
        #Verify that moving to next page is successful. 
        #Verify that the route text is correctly
        #Verify that the route has the flights
    ####
    flights_page.is_header_displayed()
    actual_header = flights_page.get_header()
    expected_header = f"Flights from {selected_departure} to {selected_destination}:"

    #Check route text
    assert actual_header == expected_header, \
    f"Expected text is {expected_header}, but got '{actual_header}'"

    #Step 5: Find how many flights displayed
    flights_count = flights_page.get_flights_count()
    assert flights_count > 0, "No flights found"

    #Step 6: Click on choose this flight button (2nd button).
    detailed_flights = flights_page.select_second_button()

    ####
        #Verify that moving to next page is successful.
        #Verify that the detailed flights header is displayed correctly
    ####
    detailed_flights.is_header_displayed()
    actual_detailed_header = detailed_flights.get_header()
    expected_detailed_header = "Your flight from TLV to SFO has been reserved."

    #Check detailed booking text
    assert actual_detailed_header == expected_detailed_header, \
    f"Expected text is {actual_detailed_header}, but got '{expected_detailed_header}'"

    #Step 7: Verify the detailed belows displayed   
    #Airlane
    actual_airline = detailed_flights.get_airline()
    expected_airline = "Airline: United"
    assert actual_airline == expected_airline, \
    f"Expected text is {actual_airline}, but got '{expected_airline}'"

    #Flight Number
    actual_flight_number = detailed_flights.get_flight_number()
    expected_flight_number = "Flight Number: UA954"
    assert actual_flight_number == expected_flight_number, \
    f"Expected text is {actual_flight_number}, but got '{expected_flight_number}'"

    #Price
    actual_price = detailed_flights.get_price()
    expected_price = "Price: 400"
    assert actual_price == expected_price, \
    f"Expected text is {actual_price}, but got '{expected_price}'"
    price_number = detailed_flights.extract_float(actual_price)


    #Fees and taxes 
    actual_fees_taxes = detailed_flights.get_fees_taxes()
    expected_fees_taxes = "Arbitrary Fees and Taxes: 514.76"
    assert actual_fees_taxes == expected_fees_taxes, \
    f"Expected text is {actual_fees_taxes}, but got '{expected_fees_taxes}'"
    fees_taxes_number = detailed_flights.extract_float(actual_fees_taxes)


    #Total
    actual_total_cost = detailed_flights.get_total_cost()
    expected_total_cost = "Total Cost: 914.76"
    assert actual_total_cost == expected_total_cost, \
    f"Expected text is {actual_total_cost}, but got '{expected_total_cost}'"
    total_cost_number = detailed_flights.extract_float(actual_total_cost)

    #Toal cost = price + fees_taxes
    total = price_number + fees_taxes_number
    assert total == total_cost_number, \
    f"Expected text is {total}, but got {total_cost_number}"
        
    #Step 8: Provide all detailed information
    detailed_flights.enter_detailed_information('Phu','423 Truong Chinh','TPHCM','Tan Binh','700000','233467346',1,2027,'PHAM NGOC PHU')
    detailed_flights.select_card_type('amex')
    detailed_flights.check_remember_me_checkbox()
    
    # Click on 'Purchase Flight' button
    detailed_purchase = detailed_flights.select_purchase_flight()

    ####
        #Verify that moving to next page is successful.
        #Verify that the detailed flights header is displayed correctly
    ####
    detailed_purchase.is_header_displayed()
    actual_detailed_purchase_header = detailed_purchase.get_header()
    expected_detailed_purchase_header = "Thank you for your purchase today!"

    # Check detailed booking text
    assert actual_detailed_purchase_header == expected_detailed_purchase_header, \
    f"Expected text is {actual_detailed_purchase_header}, but got '{expected_detailed_purchase_header}'"


    # Step 9: Verify details in the Purchase Page
    # Get actual data from the table
    actual_data_table = detailed_purchase.get_table_data()
    print(actual_data_table)

    expected_data_table = {
        'Id': '1616482160957',
        'Status': 'Pending Capture',
        'Amount': '555 USD',
        'Card Number': 'xxxxxxxxxxxx1111',
        'Expiration': '11 /2018',
        'Auth Code': '888888',
        'Date': 'Tue, 23 Mar 2021 06:49:20 +0000'
    }
    detailed_purchase.verify_table_data(actual_data_table,expected_data_table)