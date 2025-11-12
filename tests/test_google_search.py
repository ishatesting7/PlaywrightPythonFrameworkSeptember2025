import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto('https://www.google.com/')
    
    # expect(page).to_have_title("Google")

    expect(page).to_have_title(re.compile("Google",re.IGNORECASE))
    
    page.get_by_role("combobox", name="Search").fill("Playwright Test")
    page.wait_for_timeout(3000)
    
    page.keyboard.press('Enter')
    page.wait_for_timeout(3000)
    
    

