# Navigate to https://www.saucedemo.com/ and perform login after that add an item to the cart and proceed to checkout.
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[name="login-button"]')
    page.click('text=Sauce Labs Backpack')
    page.locator("[id='add-to-cart']").click();  
    page.click('[data-test="shopping-cart-link"]')
    page.click('[id="checkout"]')
    page.fill('input[name="firstName"]', 'John')
    page.fill('input[name="lastName"]', 'Doe')
    page.fill('input[name="postalCode"]', '12345')  
    page.click('[id="continue"]')
    page.click('[id="finish"]')
    # Add any additional actions or assertions here
    browser.close()
