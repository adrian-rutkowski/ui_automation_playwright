from playwright.sync_api import Page


class InventoryPage:

    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    
    def __init__(self, page: Page):
        self.page = page
        self.cart_button = page.locator(".shopping_cart_link")
        self.product_sauce_labs_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_button = page.get_by_text("Remove")

    def add_product_to_cart(self):
        self.product_sauce_labs_backpack.click()
    
    def go_to_cart(self):
        self.cart_button.click()
    
    def get_amount_of_items_in_cart(self):
        cart_badge = self.page.locator(".shopping_cart_badge")
        return cart_badge

    def remove_item_from_cart(self):
        self.remove_button.click()
    