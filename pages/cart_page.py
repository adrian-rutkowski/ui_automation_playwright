from playwright.sync_api import Page

class CartPage:

    CART_URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def go_to_checkout(self):
        self.checkout_button.click()