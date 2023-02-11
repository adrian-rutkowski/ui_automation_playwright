from playwright.sync_api import Page, expect
import pytest


class TestCart:
    def test_add_to_cart(self, login_page, inventory_page):
        login_page.open_page()
        login_page.log_in("standard_user", "secret_sauce")
        inventory_page.add_product_to_cart()
        expect(inventory_page.get_amount_of_items_in_cart()).to_have_text("1")

    def test_remove_item_from_cart(self, login_page, inventory_page):
        login_page.open_page()
        login_page.log_in("standard_user", "secret_sauce")
        inventory_page.add_product_to_cart()
        inventory_page.remove_item_from_cart()
        expect(inventory_page.get_amount_of_items_in_cart()).not_to_be_visible()
