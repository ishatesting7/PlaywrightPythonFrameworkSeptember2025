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
    
    all_demo_text_value = page.locator("//li[@id='menu-item-7128']//ul[@class='sub-menu']//a")
    print(all_demo_text_value.count())
    print(all_demo_text_value.all_inner_texts())
    elastic_menu_option = page.locator(get_header_menu_option_locator("Free Ebooks", "Tensorflow"))
    elastic_menu_option.click()
    page.wait_for_timeout(10000)
    title_page = page.title()
    print(title_page)
    assert title_page == "Free Tensorflow eBooks - GlobalSQA"

def get_header_menu_option_locator(menu_name, sub_menu_name):
    return f"//div[@class='dark_menu']//a[text()='{menu_name}']/parent::li//ul[@class='sub-menu']//a[contains(.,'{sub_menu_name}')]"
    
    # //li[@id="menu-item-7128"]//ul[@class="sub-menu"]//a
    
# //div[@class='dark_menu']//a[text()='Free Ebooks']/parent::li//[ul[@class='sub-menu']//a[contains(.,'Tensor')]

#  //div[@class='dark_menu']//a[text()='Free Ebooks']/parent::li//ul[@class='sub-menu']//a[contains(.,'Ten')]