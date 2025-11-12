import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_basic_login(page:Page):
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    

@pytest.mark.smoke
def test_basic_login2(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(5000)
    
@pytest.mark.chrome    
@pytest.mark.regression
def test_basic_login2(page:Page):
    page.goto("https://www.globalsqa.com/")
    page.wait_for_timeout(5000)

@pytest.mark.skip(reason="Skipping this test for demo")
def test_basic_login3(page:Page):
    page.goto("https://www.globalsqa.com/")
    page.wait_for_timeout(5000)

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),("locked_out_user","secret_sauce")])
def test_login_sauce_lab(page:Page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.locator("input[name='user-name']").fill(username)
    page.locator("input[name='password']").fill(password)
    page.locator("input[name='login-button']").click()
    if username == "standard_user":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    if username == "locked_out_user":
        error = page.locator("h3[data-test='error']")
        expect(error).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
@pytest.mark.xfail(reason="Known issue: Bug 101")
def test_login_sauce_lab2(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("input[name='user-name']").fill("locked_out_user")
    page.locator("input[name='password']").fill("secret_sauce")
    page.locator("input[name='login-button']").click()
    error = page.locator("h3[data-test='error']")
    expect(error).to_have_text("Epic sadface: Sorry, this user has been locked out.")

