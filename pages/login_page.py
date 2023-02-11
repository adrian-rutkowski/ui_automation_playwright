from playwright.sync_api import Page

class LoginPage:

    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def open_page(self):
        self.page.goto(self.BASE_URL)
    
    def log_in(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    