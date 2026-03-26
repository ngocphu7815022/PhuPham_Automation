import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
    )
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )


# Selct browser driver based on command line option
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    yield driver
    driver.quit()


pytest_html = None


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


# Capture screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return

        try:
            file_path = os.path.join(
                SCREENSHOT_DIR,
                f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
            )
            driver.save_screenshot(file_path)
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.png(file_path))
                report.extra = extra
        except Exception as e:
            print(f"[WARN] Screenshot hook failed: {e}")
