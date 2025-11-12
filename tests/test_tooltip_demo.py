from playwright.sync_api import Page, expect    

def test_tooltip_demo(page: Page):
    page.goto("https://jqueryui.com/tooltip/")
    
    frame = page.frame_locator(".demo-frame")
    age_input = frame.locator("#age")
    
    age_input.hover()
    
    tooltip = frame.locator(".ui-tooltip-content")
    
    expect(tooltip).to_be_visible()
    expect(tooltip).to_have_text("We ask for your age only for statistical purposes.")
    
    page.wait_for_timeout(4000)