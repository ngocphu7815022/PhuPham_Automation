from pages.base_page import BasePage
from pages.flights_page import FlightsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WelcomePage(BasePage):
    departure_city_dropdown = (By.XPATH, "//select[@name='fromPort']")
    destination_city_dropdown = (By.XPATH, "//select[@name='toPort']")
    find_flights_button = (By.XPATH, "//input[@value='Find Flights']")

    # Select Departure city
    def select_departure(self, text):
        element = self.driver.find_element(*self.departure_city_dropdown)
        select = Select(element)
        select.select_by_value(text)

    def get_departure_selected_text(self):
        element = self.driver.find_element(*self.departure_city_dropdown)
        return Select(element).first_selected_option.text

    # Select Destination city
    def select_destination(self, text):
        element = self.driver.find_element(*self.destination_city_dropdown)
        select = Select(element)
        select.select_by_value(text)

    def get_destination_selected_text(self):
        element = self.driver.find_element(*self.destination_city_dropdown)
        return Select(element).first_selected_option.text

    # Click on 'Find Flights' button
    def select_find_flights(self):
        self.driver.find_element(*self.find_flights_button).click()
        # WAIT cho page mới load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h3"))
        )
        return FlightsPage(self.driver)
