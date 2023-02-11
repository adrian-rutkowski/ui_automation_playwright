from playwright.sync_api import Page, expect
import pytest

class TestE2E:
    @pytest.mark.wip
    def test_checkout_order(self, login_page, inventory_page, cart_page, checkout_page):
        login_page.open_page()
        login_page.log_in("standard_user", "secret_sauce")
        inventory_page.add_product_to_cart()
        inventory_page.go_to_cart()
        cart_page.go_to_checkout()
        checkout_page.enter_details_and_proceed("First", "Last", "90210")
        checkout_page.click_finish()
        expect(checkout_page.pony_express_logo).to_be_visible()
        
