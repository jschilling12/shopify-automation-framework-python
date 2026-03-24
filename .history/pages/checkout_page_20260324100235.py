from playwright.sync_api import Page, expect
from checkout_selectors import CheckoutSelectors

# Checkout process works across all Shopify sites, in the checkout menu (unless personally customized).

class CheckoutProcess:
    def __init__(self, page:Page, selectors: CheckoutSelectors):
        self.page = page
        self.add_to_cart = page.get_by_role("button", name=selectors.add_to_cart)
        self.checkout_select = page.get_by_role("button", name=selectors.checkout)
        self.account = page.get_by_role("textbox", name=selectors.account)
        self.card_number = page.frame_locator(selectors.card_number_frame).get_by_role(
            "textbox", name="Card number"
        )
        self.exp_date = page.frame_locator(selectors.exp_date_frame).get_by_role(
            "textbox", name="Expiration date (MM / YY)"
        )
        self.sec_code = page.frame_locator(selectors.sec_code_frame).get_by_role(
            "textbox", name="Security code"
        )
        self.card_name = page.frame_locator(selectors.card_name_frame).get_by_role(
            "textbox", name="Name on card"
        )
        self.customer_name_first = page.get_by_role("textbox", name=selectors.customer_name_first)
        self.customer_name_last = page.get_by_role("textbox", name=selectors.customer_name_last)
        self.customer_address = page.get_by_role("combobox", name=selectors.customer_address)
        self.pay = page.get_by_role("button", name=selectors.pay)
        self.homepage = page.get_by_role("link", name=selectors.homepage)
    
    def checkout_button(self):
        self.add_to_cart.click()
        self.checkout_select.click()

    def account_email(self, email):
        self.account.fill(email)

    def card_details(self, num, exp, sec, name):
        self.card_number.fill(num)
        self.exp_date.fill(exp)
        self.sec_code.fill(sec)
        self.card_name.fill(name)

    def customer_details(
            self, 
            first, 
            last, 
            customer_address, 
            customer_address_option
    ):
        
        self.customer_name_first.fill(first)
        self.customer_name_last.fill(last)
        self.customer_address.fill(customer_address)
        
        # Dropdown selector for the address fill.
        self.page.get_by_role("option", name=customer_address_option).click()
        self.page.wait_for_timeout(2000)
    
    def pay_now(self):
        self.pay.click()

    def continue_shopping(self):
        expect(self.homepage).to_be_visible(timeout=15000)
        self.homepage.click()

    def checkout(
            self, 
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
        
        self.checkout_button()
        self.account_email(email)
        self.card_details(num, exp, sec, name)
        self.customer_details(first, last, customer_address, customer_address_option)
        self.pay_now()
        self.continue_shopping()
    