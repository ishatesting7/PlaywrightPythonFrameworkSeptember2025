import pytest
from playwright.sync_api import Page, expect, sync_playwright

def test_web_table_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo3x.opencartreports.com/admin/")
    
        page.locator("input#input-username").fill("demo")
        page.locator("input#input-password").fill("demo")
        page.locator("button[type='submit']").click()
        page.wait_for_timeout(5000)
        page.locator('[href="#collapse5"]').click()
        page.wait_for_timeout(2000)
        page.locator("//ul[@id='collapse5']//a[contains(text(),'Customers')]").click()
        page.wait_for_timeout(5000) 
    
        rows = page.locator("tbody tr") # 15 Locators
    
        index = 0
        while(index < rows.count()):
                company_name = rows.nth(index).inner_text()
                print(company_name)
                index += 1
    