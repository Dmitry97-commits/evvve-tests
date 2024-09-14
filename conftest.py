import json
import os

import pytest
from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.main_page import MainPage
from pages.shopping_cart_page import ShoppingCartPage

test_results = []


def pytest_addoption(parser):
    parser.addoption(
        "--webdriver", action="store", default="local", help="one of: remote, local"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        test_result = {
            "test_name": item.nodeid,
            "outcome": result.outcome,
            "error": str(result.longrepr) if result.failed else None
        }
        test_results.append(test_result)


@pytest.fixture(scope="session", autouse=True)
def create_report(request):
    def fin():
        if test_results:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Test Results"
            sheet.append(["Test Name", "Outcome", "Error Message"])
            for result in test_results:
                sheet.append([result["test_name"], result["outcome"], result["error"]])
            excel_report = 'test_report.xlsx'
            workbook.save(excel_report)

    request.addfinalizer(fin)


def get_configs(name_value: str):
    with open("configurations.json") as file:
        return json.load(file)[name_value]


@pytest.fixture(scope="session")
def option_webdriver(request):
    return request.config.getoption("--webdriver")


@pytest.fixture(scope="function")
def driver(option_webdriver):
    _driver: WebDriver
    if option_webdriver == "remote":
        _driver = webdriver_remote()
    else:
        _driver = webdriver_local()
    _driver.set_window_size(1920, 1080)
    yield _driver
    _driver.quit()


def webdriver_remote():
    raise NotImplementedError


def webdriver_local() -> WebDriver:
    chrome_install = ChromeDriverManager().install()
    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")
    service = ChromeService(chromedriver_path)
    browser = webdriver.Chrome(service=service)
    return browser


@pytest.fixture(scope="function")
def navigate_to_demowebshop(driver):
    driver.get(get_configs("base_url"))
    return MainPage(driver)


def navigate_to_cart(driver):
    driver.get(get_configs("cart_url"))
    return ShoppingCartPage(driver)
