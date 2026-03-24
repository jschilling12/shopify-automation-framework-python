import sys
import os
import pytest
from playwright.sync_api import sync_playwright
from checkout_selectors import CheckoutSelectors
from addtocart_selectors import AddtocartSelectors

# Pytest fixture for Playwright page object, to be used across all tests.

sys.path.insert(0, os.path.dirname(__file__))

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://gamedaytldr.live/")
        yield page
        context.close()
        browser.close()

@pytest.fixture
def text_teamname():
    return "USA"

@pytest.fixture
def dropdown_teamname():
    return "Arsenal"

@pytest.fixture
def email():
    return "fakeemail@gmail.com"

@pytest.fixture
def num():
    return "1"

@pytest.fixture
def exp():
    return "03/30"

@pytest.fixture
def sec():
    return "111"

@pytest.fixture
def name():
    return "1"

@pytest.fixture
def first():
    return "Jordan"

@pytest.fixture
def last():
    return "Schilling"

@pytest.fixture
def customer_address():
    return "111"

@pytest.fixture
def customer_address_option():
    return "111 North Orange Ave"

@pytest.fixture
def add_to_cart_sel():
    return AddtocartSelectors(
        selection_input=".promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
        selection_input_promo=".promo-option-card-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > .promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > .promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
        promo_toggle=".epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
        promo_body="#epl-body-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
        promo_email="#epl-email-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
        email="Email Address *",
        team="Favourite Team *",
        dropdown="Favourite EPL Team *",
        cart="Add to Cart",
    )

@pytest.fixture
def checkout_sel():
    return CheckoutSelectors(
        add_to_cart="Add to Cart",
        checkout="Check out",
        account="Email",
        card_number_frame='iframe[name^="card-fields-number-"]',
        exp_date_frame='iframe[name^="card-fields-expiry-"]',
        sec_code_frame='iframe[name^="card-fields-verification_value-"]',
        card_name_frame='iframe[name^="card-fields-name-"]',
        customer_name_first="First name",
        customer_name_last="Last name",
        customer_address="Address",
        pay="Pay now",
        homepage="Continue shopping",
    )