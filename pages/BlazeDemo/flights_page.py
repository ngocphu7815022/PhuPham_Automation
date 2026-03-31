from pages.base_page import BasePage
from pages.BlazeDemo.detailed_flights_page import DetailedPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FlightsPage(BasePage):
    header = (By.XPATH, "//h3[normalize-space()='Flights from Portland to London:']")
    flights_rows = (By.XPATH, "//table/tbody/tr")
    second_button = (By.XPATH, "//tbody/tr[2]/td[1]/input[1]")

    # Check moved to flights booking page
    def is_header_displayed(self):
        return self.is_visible(self.header)

    # Get header
    def get_header(self):
        return self.get_text(self.header)

    @allure.step("Verify that route has flights")
    def get_flights_count(self):
        rows = self.driver.find_elements(*self.flights_rows)
        return len(rows)

    @allure.step("Select second 'Choose This Flight' button")
    def select_second_button(self):
        self.driver.find_element(*self.second_button).click()
        # WAIT cho page mới load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h2[normalize-space()='Your flight from TLV to SFO has been reserved.']",
                )
            )
        )
        return DetailedPage(self.driver)
