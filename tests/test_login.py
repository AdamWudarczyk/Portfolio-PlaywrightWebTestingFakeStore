import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

URL = "https://fakestore.testelka.pl/moje-konto/"

@pytest.mark.login
def test_login_with_valid_credentials(page, user_data):
    login_page = LoginPage(page)
    login_page.go_to(URL)

    login_page.login(
        user_data["valid_user"]["username"],
        user_data["valid_user"]["password"]
    )

    # Sprawdzamy tekst powitania
    greeting = page.locator(".woocommerce-MyAccount-content").nth(0)
    expect(greeting).to_contain_text("Witaj automationtesting539")