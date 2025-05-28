import pytest
from pages.shop_page import ShopPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

SHOP_URL = "https://fakestore.testelka.pl/shop/"

@pytest.mark.cart
def test_product_added_is_visible_in_cart(page):
    shop = ShopPage(page)
    shop.go_to(SHOP_URL)

    shop.open_windsurfing_category()
    shop.add_first_product_to_cart()

    expect(shop.cart_count).to_have_text("1 Produkt", timeout=5000)

    shop.open_cart()

    cart = CartPage(page)
    cart.expect_cart_not_empty()

    name = cart.get_first_item_name()
    quantity = cart.get_first_item_quantity()

    print(f"Produkt w koszyku: {name}, ilość: {quantity}")

    assert name != ""
    assert int(quantity) >= 1

@pytest.mark.cart
def test_remove_product_from_cart(page):
    shop = ShopPage(page)
    shop.go_to(SHOP_URL)
    shop.open_windsurfing_category()
    shop.add_first_product_to_cart()
    expect(shop.cart_count).to_have_text("1 Produkt", timeout=5000)

    shop.open_cart()
    cart = CartPage(page)
    cart.expect_cart_not_empty()

    cart.remove_first_product()
    cart.expect_cart_is_empty()