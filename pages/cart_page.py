from pages.base_page import BasePage
from playwright.sync_api import expect
import re

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.first_item_name = self.cart_items.first.locator(".product-name a")
        self.first_item_quantity = self.cart_items.first.locator(".quantity input")
        self.remove_first_item_button = self.cart_items.first.locator(".product-remove a")
        self.empty_cart_message = page.locator(".cart-empty")

    def expect_cart_not_empty(self):
        expect(self.cart_items).to_have_count(1, timeout=5000)

    def get_first_item_name(self):
        return self.first_item_name.inner_text()

    def get_first_item_quantity(self):
        return self.first_item_quantity.input_value()

    def remove_first_product(self):
        self.remove_first_item_button.click()

    def expect_cart_is_empty(self):
        expect(self.empty_cart_message).to_be_visible(timeout=5000)

    def proceed_to_checkout(self):
        self.page.locator(".checkout-button").click()

    def expect_on_checkout_page(self):
        expect(self.page).to_have_url(re.compile(".*/zamowienie/?$"), timeout=5000)

