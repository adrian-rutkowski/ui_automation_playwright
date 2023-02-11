from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("#first-name")
        self.last_name_field = page.locator("#last-name")
        self.zip_code_field = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.pony_express_logo = page.locator(".pony_express")
    
    def enter_first_name(self, first_name):
        self.first_name_field.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name_field.fill(last_name)
        
    def enter_zip_code(self, zip_code):
        self.zip_code_field.fill(zip_code)

    def click_continue(self):
        self.continue_button.click()
    
    def enter_details_and_proceed(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        self.click_continue()
    
    def click_finish(self):
        self.finish_button.click()
    
