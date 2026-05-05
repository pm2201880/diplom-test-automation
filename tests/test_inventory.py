import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import STANDARD_USER, PASSWORD


class TestInventory:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(STANDARD_USER, PASSWORD)

    def test_sorting_by_price_low_to_high(self, page):
        inventory = InventoryPage(page)
        inventory.sort_by("lohi")
        prices = inventory.get_price_numbers()
        for i in range(len(prices) - 1):
            assert prices[i] <= prices[i + 1], f"Sorting error: {prices[i]} > {prices[i + 1]}"