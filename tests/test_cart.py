import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import STANDARD_USER, PASSWORD


class TestCart:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(STANDARD_USER, PASSWORD)

    def test_add_and_remove_item(self, page):
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        assert inventory.get_cart_badge_text() == "1"
        inventory.go_to_cart()

        cart = CartPage(page)
        assert not cart.is_empty()
        cart.remove_item("sauce-labs-backpack")
        assert cart.is_empty()