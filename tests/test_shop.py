import pytest
from pages.shop_page import ShopPage
from playwright.sync_api import expect

SHOP_URL = "https://fakestore.testelka.pl/shop/"


@pytest.mark.shop
def test_add_first_product_from_windsurfing_to_cart(page):
    shop = ShopPage(page)
    shop.go_to(SHOP_URL)


    shop.open_windsurfing_category()
    assert shop.products.count() > 0
    shop.add_first_product_to_cart()
    expect(shop.cart_icon).to_contain_text("1 Produkt")