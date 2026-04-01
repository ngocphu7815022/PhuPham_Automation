from pages.base_page import BasePage
from pages.BlazeDemo.detailed_purchase_page import DetailedPurchasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import allure


class DetailedPage(BasePage):
    header = (By.XPATH, "//h2")
    airline_text = (By.XPATH, "//p[normalize-space()='Airline: United']")
    flight_number_text = (By.XPATH, "//p[normalize-space()='Flight Number: UA954']")
    price_text = (By.XPATH, "//p[normalize-space()='Price: 400']")
    fees_taxes_text = (
        By.XPATH,
        "//p[normalize-space()='Arbitrary Fees and Taxes: 514.76']",
    )
    total_cost_text = (By.XPATH, "/html[1]/body[1]/div[2]/p[5]")
    name_textbox = (By.XPATH, "//input[@id='inputName']")
    address_textbox = (By.XPATH, "//input[@id='address']")
    city_textbox = (By.XPATH, "//input[@id='city']")
    state_textbox = (By.XPATH, "//input[@id='state']")
    zip_code_textbox = (By.XPATH, "//input[@id='zipCode']")
    card_type_dropdown = (By.XPATH, "//select[@id='cardType']")
    card_number_textbox = (By.XPATH, "//input[@id='creditCardNumber']")
    month_textbox = (By.XPATH, "//input[@id='creditCardMonth']")
    year_textbox = (By.XPATH, "//input[@id='creditCardYear']")
    name_on_card_textbox = (By.XPATH, "//input[@id='nameOnCard']")
    remember_me_checkbox = (By.XPATH, "//input[@id='rememberMe']")
    purchase_flight_butotn = (By.XPATH, "//input[@value='Purchase Flight']")

    def is_header_displayed(self):
        return self.is_visible(self.header)

    def get_header(self):
        return self.get_text(self.header)

    def get_airline(self):
        return self.get_text(self.airline_text)

    def get_flight_number(self):
        return self.get_text(self.flight_number_text)

    def get_price(self):
        return self.get_text(self.price_text)

    def get_fees_taxes(self):
        return self.get_text(self.fees_taxes_text)

    def get_total_cost(self):
        return self.get_text(self.total_cost_text)

    @allure.step("Enter detailed information")
    def enter_detailed_information(
        self,
        name,
        address,
        city,
        state,
        zip_code,
        credit_card_number,
        month,
        year,
        name_on_card,
    ):
        self.type(self.name_textbox, name)
        self.type(self.address_textbox, address)
        self.type(self.city_textbox, city)
        self.type(self.state_textbox, state)
        self.type(self.zip_code_textbox, zip_code)
        self.type(self.card_number_textbox, credit_card_number)
        self.type(self.month_textbox, month)
        self.type(self.year_textbox, year)
        self.type(self.name_on_card_textbox, name_on_card)

    def select_card_type(self, text):
        element = self.driver.find_element(*self.card_type_dropdown)
        select = Select(element)
        select.select_by_value(text)

    def check_remember_me_checkbox(self):
        if not self.is_selected(self.remember_me_checkbox):
            self.click(self.remember_me_checkbox)

    def select_purchase_flight(self):
        self.driver.find_element(*self.purchase_flight_butotn).click()
        # WAIT cho page mới load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        return DetailedPurchasePage(self.driver)

    # Extract number from text
    def extract_float(self, text: str) -> float:
        match = re.search(r"\d+(?:\.\d+)?", text)
        return float(match.group()) if match else None
