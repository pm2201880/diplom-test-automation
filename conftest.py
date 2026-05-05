import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--browser", action="append", default=[],
                     help="Браузеры для запуска: chromium, firefox, webkit")


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser")
        if not browsers:
            browsers = ["chromium"]
        metafunc.parametrize("browser_name", browsers, scope="session")


@pytest.fixture(scope="function")
def page(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()