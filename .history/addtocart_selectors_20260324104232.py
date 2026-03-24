from dataclasses import dataclass

# Config

@dataclass
class AddtocartSelectors:
    selection_input: str
    selection_input_promo: str
    promo_toggle: str
    promo_body: str
    email: str
    team: str
    dropdown: str
    cart: str