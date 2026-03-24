
from playwright.sync_api import Page
from pages.add_to_cart_page import AddToCartProcess
from pages.checkout_page import CheckoutProcess


# Orchestration layer for Pytest functions


def test_add_to_cart(
        page:Page, 
        add_to_cart_sel,
        email, 
        text_teamname, 
        dropdown_teamname
):
    cart_flow = AddToCartProcess(page, add_to_cart_sel)
    cart_flow.add_to_cart(email, text_teamname, dropdown_teamname)

def test_checkout(
        page:Page,
        text_teamname, 
        add_to_cart_sel,
        checkout_sel,
        dropdown_teamname, 
        email, 
        num, 
        exp, 
        sec, 
        name, 
        first, 
        last, 
        customer_address, 
        customer_address_option
):
    
    cart_flow = AddToCartProcess(page, add_to_cart_sel)
    cart_flow.add_to_cart(email, text_teamname, dropdown_teamname)

    checkout = CheckoutProcess(page, checkout_sel)
    checkout.checkout(
        email, 
        num, 
        exp, 
        sec, 
        name, 
        first, 
        last, 
        customer_address, 
        customer_address_option
    )
    # expect(page.get_by_role("button", name="Pay now")).to_be_visible()