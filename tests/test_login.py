import pytest
from pages.login_page import LoginPage
from data.test_data import STANDARD_USER, LOCKED_OUT_USER, PASSWORD


class TestLogin:
    def test_positive_login(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(STANDARD_USER, PASSWORD)
        assert "inventory" in page.url

    def test_negative_login(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(LOCKED_OUT_USER, PASSWORD)
        error = login_page.get_error_text()
        assert "locked out" in error.lower()
        