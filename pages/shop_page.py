from pages.base_page import BasePage

class ShopPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.windsurfing_category = page.locator("a:has-text('Windsurfing')").nth(0)
        self.products = page.locator("ul.products li")
        self.first_product_add_button = self.products.first.locator(".button")
        self.cart_icon = page.locator(".cart-contents")
        self.cart_count = page.locator(".cart-contents .count")

    def open_windsurfing_category(self):
        self.windsurfing_category.click()

    def add_first_product_to_cart(self):
        self.first_product_add_button.click(force=True)

    def open_cart(self):
        self.cart_icon.click()