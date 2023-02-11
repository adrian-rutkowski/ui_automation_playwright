from playwright.sync_api import Page, expect
import pytest


class TestLogin:
    @pytest.mark.smoke
    def test_sign_in_valid(self, page: Page, login_page, inventory_page):
        # Navigate to the login page
        login_page.open_page()

        # Type username
        # Type password
        # Click login button
        login_page.log_in("standard_user", "secret_sauce")

        # Verify the cart button is visible
        expect(inventory_page.cart_button).to_be_visible()

        # Verify the URL matches the inventory page
        expect(page).to_have_url(inventory_page.INVENTORY_URL)

    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "invalidpw"),
            ("invalid_user", "secret_sauce"),
            ("", "secret_sauce"),
            ("standard_user", ""),
        ],
    )
    def test_sign_in_invalid(self, page: Page, login_page, username, password):
        login_page.open_page()
        login_page.log_in(username, password)
        expect(login_page.error_message).to_be_visible()
