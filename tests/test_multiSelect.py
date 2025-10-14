import re
from playwright.sync_api import Page, expect

def test_multi_select_dropdown(page: Page):
    page.goto('https://selenium08.blogspot.com/2019/11/dropdown.html')
    
    multi_select = page.locator('select[name="Month"]')
    multi_select.click()
    
    multi_select.select_option(["Feb","May","June"])
    page.wait_for_timeout(2000)
    
    expect(multi_select).to_have_values(["Feb","May","June"])
    # expect(multi_select).to_have_values([re.compile(r"F"),re.compile(r"M"),re.compile(r"J")])
    
    

#https://selenium08.blogspot.com/2019/11/dropdown.html