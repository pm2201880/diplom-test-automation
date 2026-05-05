class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator("[data-test='inventory-item']")
        self.prices = page.locator("[data-test='inventory-item-price']")
        self.add_to_cart_buttons = page.locator("[data-test^='add-to-cart']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def sort_by(self, value):
        self.sort_dropdown.select_option(value)

    def get_prices(self):
        return self.prices.all_inner_texts()

    def get_price_numbers(self):
        return self.page.eval_on_selector_all(
            "[data-test='inventory-item-price']",
            "elements => elements.map(el => parseFloat(el.textContent.replace('$', '')))"
        )

    def add_item_to_cart(self, item_name):
        item_name_selector = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='add-to-cart-{item_name_selector}']").click()

    def get_cart_badge_text(self):
        return self.cart_badge.text_content()

    def go_to_cart(self):
        self.cart_link.click()

    def is_loaded(self):
        return "inventory" in self.page.url