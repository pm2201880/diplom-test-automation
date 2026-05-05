import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import STANDARD_USER, PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE


class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(STANDARD_USER, PASSWORD)

    def test_full_checkout(self, page):
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.go_to_checkout()

        checkout = CheckoutPage(page)
        checkout.fill_shipping_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
        checkout.continue_checkout()
        checkout.finish_checkout()
        assert checkout.is_complete()