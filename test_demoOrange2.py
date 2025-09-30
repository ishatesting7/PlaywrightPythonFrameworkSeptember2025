import pytest

@pytest.mark.parametrize("username,password", [
    ("Admin", "admin123")
])
def test_orangehrm_login_logout(page, username, password):
    # Step 1: Open the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Enter credentials
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')

    # Step 3: Verify Dashboard loaded
    page.wait_for_selector("h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
    assert page.inner_text("h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module") == "Dashboard"

    # Step 4: Click on Profile Icon
    page.click('span.oxd-userdropdown-tab')

    # Step 5: Click Logout
    page.click('text=Logout')

    # Step 6: Verify back on Login Page
    page.wait_for_selector('input[name="username"]')
    assert page.is_visible('input[name="username"]')
# pytest -v --headed test_orangehrm_login_logout.py
# pytest -v --browser=chromium
# pytest -v --browser=firefox
# pytest -v --browser=webkit