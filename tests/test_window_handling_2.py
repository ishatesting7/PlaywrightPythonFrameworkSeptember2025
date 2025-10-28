from playwright.sync_api import sync_playwright,expect, Playwright

def rum(playwright:Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    with page.expect_popup() as popup_info:
        page.locator("text=Click Here").click()
    page1 = popup_info.value
    
    new_window_txt = page1.locator(".example h3")
    print(new_window_txt.inner_text())
    expect(new_window_txt).to_have_text("New Window")
    
    page1.title();
    
        
        
    
    
   