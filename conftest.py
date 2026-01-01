import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    driver.maximize_window()
    yield driver
    driver.quit()