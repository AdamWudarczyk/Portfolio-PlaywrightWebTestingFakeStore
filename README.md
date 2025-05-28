# 🎭 Playwright Web Testing – FakeStore (Testelka)

This is an end-to-end (E2E) test automation project using [Playwright](https://playwright.dev/python/) with Python for the demo store:  
👉 https://fakestore.testelka.pl/

---

## Technologies & Tools

-  Python 3.10+
-  Playwright 1.52+
-  Pytest
-  Page Object Model (POM)
-  Pytest HTML Report / Allure (optional)
-  JSON Fixtures
-  Git, GitHub

---

##  Test Scenarios

###  Account (Login)
-  Login with valid credentials
-  Login with invalid credentials

### Shop
-  Displaying product list
-  Adding a product to the cart
-  Filtering by category (WIP)
-  Cart & Checkout process (WIP)

---

##  How to Run Tests

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2. Run all tests

```bash
pytest -v
```

### 3. Run tests with HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```
### 4. Run by tag (marker)

```bash
pytest -m login     # Login tests
pytest -m shop      # Shop page tests
pytest -m cart      # Cart functionality
pytest -m e2e       # Full end-to-end flow
```

## Project Structure

Portfolio-PlaywrightWebTestingFakeStore/\
├── conftest.py\
├── fixtures/\
│   └── user_data.json\
├── pages/\
│   ├── base_page.py\
│   ├── login_page.py\
│   └── shop_page.py\
│   └── cart_page.py\
├── tests/\
│   ├── test_login.py\
│   ├── test_shop.py\
│   ├── test_cart.py\
│   └── test_e2e.py\
├── reports/\
├── .gitignore\
├── pytest.ini\
├── requirements.txt\
└── README.md\

### Future Plans

Add more various tests! 

____
Created by Adam Wudarczyk