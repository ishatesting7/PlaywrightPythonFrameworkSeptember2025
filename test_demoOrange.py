import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("username,password", [
    ("Admin", "admin123")
])
def test_orangehrm_login_logout(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # set True for headless
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open the URL
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.locator('input[name="username"]').click()
        
        page.click('input[name="username"]')
        
        page.fill('input[name="username"]', "DemoUser")

        page.locator().fill('input[name="username"]', "DemoUser")






        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')

        page.wait_for_selector("h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
        assert page.inner_text("h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module") == "Dashboard"

        page.click('span.oxd-userdropdown-tab')

        page.click('text=Logout')

        page.wait_for_selector('input[name="username"]')
        assert page.is_visible('input[name="username"]')

        context.close()
        browser.close()
