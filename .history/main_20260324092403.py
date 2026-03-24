from playwright.sync_api import sync_playwright
from pages.add_to_cart_page import AddToCartProcess
from pages.checkout_page import CheckoutProcess
from addtocart_selectors import AddtocartSelectors
from checkout_selectors import CheckoutSelectors

# Composition and entry point for the test suite. This is where we can set up test data and call the tests.

BASE_URL = "https://gamedaytldr.live/"

# World Cup Team
TEXT_TEAMNAME = 'USA'

# Dropdown for Premier League team
DROPDOWN = 'Arsenal'
EMAIL = 'fakeeamil@gmail.com'
NUM = '1'
EXP = '03/30'
SEC = '111'
NAME = '1'
FIRST = 'Jordan'
LAST = 'Schilling'
CUSTOMER_ADDRESS = '111'

# Selection for address dropdown
CUSTOMER_ADDRESS_OPTION = '111 North Orange Ave'

add_to_cart_sel = AddtocartSelectors(
    selection_input= ".promo-option-indicator-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    selection_input_promo= ".promo-option-card-" \
        "aodrsmzfpyxdet0hvraigenblock388c186ytkrd9.is-radio > " \
        ".promo-option-inner-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9 > "
        ".promo-option-indicator-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_toggle=".epl-optin-toggle-checkbox-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_body ="#epl-body-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    promo_email="#epl-email-aodrsmzfpyxdet0hvraigenblock388c186ytkrd9",
    email= "Email Address *",
    team= "Favourite Team *",
    dropdown= "Favourite EPL Team *",
    cart= "Add to Cart"
)

checkout_selectors = CheckoutSelectors(
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


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        

        try:
            page.goto(BASE_URL)

            cart_flow = AddToCartProcess(page, add_to_cart_sel)
            cart_flow.add_to_cart(
                EMAIL,
                TEXT_TEAMNAME, 
                DROPDOWN,
            )

            checkout_flow = CheckoutProcess(page, checkout_selectors)
            checkout_flow.checkout(
                EMAIL, 
                NUM, 
                EXP, 
                SEC, 
                NAME, 
                FIRST, 
                LAST,
                CUSTOMER_ADDRESS, 
                CUSTOMER_ADDRESS_OPTION
            )

        except Exception as e:
            print(f"Error occurred: {e}")
            
        finally:
            context.close()
            browser.close()
        

if __name__ == "__main__":
    main()