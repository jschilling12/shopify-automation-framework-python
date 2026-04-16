# Shopify Automation Framework (Playwright + Python)

A lightweight, production-style **end-to-end automation framework** for Shopify storefronts, built with a focus on **maintainability and scalability using the Page Object Model (POM)**.

---

## Tech Stack

* **Playwright (Python)**
* **Pytest**
* Shopify storefront (real-world flows)
* Custom utilities (selectors, test data, helpers)

---

## Architecture (POM)

The framework uses the **Page Object Model (POM)** to separate test logic from UI interactions.

```
/pages
  ├── base_page.py
  ├── product_page.py
  ├── cart_page.py
  ├── checkout_page.py

/tests
  ├── test_checkout_flow.py
  ├── test_add_to_cart.py

/utils
  ├── selectors.py
  ├── test_data.py
  ├── helpers.py
```

---

## Page Object Model (POM)

Each page object:

* Encapsulates **selectors**
* Defines **user actions**
* Exposes **clean, reusable methods**

**Instead of:**

```python
page.click("button.add-to-cart")
page.fill("#email", "test@test.com")
```

**Using POM:**

```python
product_page.add_to_cart()
checkout_page.enter_email("test@test.com")
```

---

### Example: Page Object

```python
class ProductPage(BasePage):
    def add_to_cart(self):
        self.page.locator(self.selectors.ADD_TO_CART).click()
```

---

### Example: Handling Shopify Checkout (iframes)

```python
class CheckoutPage(BasePage):
    def enter_payment_info(self, card):
        frame = self.page.frame_locator("iframe[name^='card-fields']")
        frame.locator("#number").fill(card.number)
```

---

## Example Test

```python
def test_user_can_complete_checkout(page):
    product = ProductPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    product.navigate()
    product.add_to_cart()

    cart.open()
    cart.proceed_to_checkout()

    checkout.fill_shipping_info(user)
    checkout.complete_payment(card)

    assert checkout.is_order_confirmed()
```

---

## Running the Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2. Run tests

```bash
pytest
```

---

## CI Integration (GitHub Actions)

Tests run automatically on every push and pull request using GitHub Actions.

### Workflow File

Create:

```
.github/workflows/tests.yml
```

```yaml
name: Playwright Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps

      - name: Run tests
        run: pytest
```

---

## What This Adds

* Validates tests on every PR
* Ensures Playwright + dependencies install cleanly
* Catches regressions in checkout flows early

---

## Summary (Updated)

* POM-based architecture for maintainability
* Playwright + Pytest stack
* Handles Shopify iframe checkout flows
* Runs locally and in CI via GitHub Actions
