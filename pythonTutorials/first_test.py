#open a webpage and enter the username and password
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/login")
    page.fill('input[name="username"]', 'my_username')
    page.fill('input[name="password"]', 'my_password')
    page.click('button[type="submit"]')
    # Add any additional actions or assertions here
    browser.close()