class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator("[data-test='inventory-item']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def get_items_count(self):
        return self.cart_items.count()

    def remove_item(self, item_name):
        item_name_selector = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='remove-{item_name_selector}']").click()

    def go_to_checkout(self):
        self.checkout_button.click()

    def is_empty(self):
        return self.get_items_count() == 0