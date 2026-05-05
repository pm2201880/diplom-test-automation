class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_field = page.locator("[data-test='firstName']")
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")
        self.back_home_button = page.locator("[data-test='back-to-products']")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_complete_header_text(self):
        return self.complete_header.text_content()

    def is_complete(self):
        return "Thank you" in self.get_complete_header_text()