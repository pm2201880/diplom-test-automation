class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.text_content()