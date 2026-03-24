from playwright.sync_api import Page
from addtocart_selectors import AddtocartSelectors

#Add_to_Cart ONLY works on the Polished Products Shopify template.

class AddToCartProcess:
    def __init__(self, page:Page, selectors: AddtocartSelectors):
        self.page = page
        self.selectors = selectors
        self.selection_input = page.locator(selectors.selection_input)
        self.selection_input_promo = page.locator(selectors.selection_input_promo)
        self.email = page.get_by_role("textbox", name=selectors.email)
        self.team_textbox = page.get_by_role("textbox", name=selectors.team)
        self.team_dropdown = page.get_by_label(selectors.dropdown)
        self.cart = page.get_by_role("button", name=selectors.cart)

    def select_input(self):
        self.selection_input.first.click()

    def select_input_promo(self, promo_toggle):
        self.page.locator(promo_toggle).click()
        self.selection_input_promo.first.click()

    def input_email(self, email):
        self.page.get_by_text("✉️ Email").first.click()
        promo_email = self.page.locator(self.selectors.promo_email)

        # Prefer the promo email field when it is rendered and visible.
        if promo_email.count() > 0 and promo_email.first.is_visible():
            promo_email.first.fill(email)
            return

        email_boxes = self.page.get_by_role("textbox", name=self.selectors.email)
        email_count = email_boxes.count()

        # When multiple email fields exist, fill the first visible one.
        for i in range(email_count):
            candidate = email_boxes.nth(i)
            if candidate.is_visible():
                candidate.fill(email)
                return

        email_boxes.first.fill(email)

    def input_team(self, text_teamname):
        self.team_textbox.fill(text_teamname)

    def select_team(self, teamname):
        self.team_dropdown.wait_for(state="visible")
        self.team_dropdown.select_option(label=teamname)
    
    def select_cart(self):
        self.cart.click()

    def add_to_cart(self, email, text_teamname, dropdown_teamname):
        self.select_input()
        self.select_input_promo(self.selectors.promo_toggle)
        self.select_team(dropdown_teamname)
        self.input_email(email)
        self.input_team(text_teamname)
        self.select_cart()