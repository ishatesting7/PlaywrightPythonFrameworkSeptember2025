from playwright.sync_api import Page, expect

def test_validating_property(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    login_btn = page.get_by_text("Login")
    
    #expect(login_btn).to_have_css("background-color", "rgb(61, 220, 145")
    expect(login_btn).to_have_css("font-size", "16px")
    expect(login_btn).to_have_css("height", "32px")
    expect(login_btn).to_have_css("line-height", "normal")