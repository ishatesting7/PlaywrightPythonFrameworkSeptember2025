from playwright.sync_api import sync_playwright, Playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    context2 = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to the initial page
    page.goto("https://the-internet.herokuapp.com/windows")

    # Click the link that opens a new window
    page2 = context2.new_page()
    page2.goto("https://www.python.org/")
    page3 = context2.new_page()
    page3.goto("https://www.wikipedia.org/")    
    
    context.close()
    context2.close()
    browser.close()
    
with sync_playwright() as playwright:
    run(playwright)