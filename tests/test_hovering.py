import re
from playwright.sync_api import Page, expect

def test_hovering(page: Page):
    page.goto("https://www.globalsqa.com/demo-site/")
    menu_free_ebook = page.locator("#menu-item-7128",has_text="Free Ebooks")
    
    print(menu_free_ebook.inner_text())

    menu_free_ebook.hover()
    
    page.wait_for_timeout(5000)
    
def test_hover_and_select(page: Page):
    page.goto("https://www.globalsqa.com/demo-site/")
    menu_free_ebook = page.locator("#menu-item-7128",has_text="Free Ebooks")
    menu_free_ebook.hover()
    
    page.wait_for_timeout(3000)
    
    # //li[@id="menu-item-7128"]//ul[@class="sub-menu"]//a
    
    
    