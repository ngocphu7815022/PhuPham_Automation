from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DetailedPurchasePage(BasePage):
    header = (By.XPATH, "//h1[normalize-space()='Thank you for your purchase today!']")

    def is_header_displayed(self):
        return self.is_visible(self.header)

    def get_header(self):
        return self.get_text(self.header)

    def get_table_data(self):
        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")
        data = {}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                data[key] = value
        return data

    def verify_table_data(self, actual_data, expected_data):
        errors = []

        for key, expected_value in expected_data.items():
            if key not in actual_data:
                errors.append(f"{key} not found")
                continue

            actual_value = actual_data[key]
            if actual_value != expected_value:
                errors.append(f"{key}: expected {expected_value}, got {actual_value}")
        assert not errors, ";\n".join(errors)
