import pytest
from pages.shop_page import ShopPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

SHOP_URL = "https://fakestore.testelka.pl/shop/"

@pytest.mark.e2e
def test_full_checkout_process(page):
    shop = ShopPage(page)
    shop.go_to(SHOP_URL)

    shop.open_windsurfing_category()
    shop.add_first_product_to_cart()
    expect(shop.cart_count).to_have_text("1 Produkt", timeout=5000)

    shop.open_cart()

    cart = CartPage(page)
    cart.expect_cart_not_empty()
    cart.proceed_to_checkout()
    cart.expect_on_checkout_page()