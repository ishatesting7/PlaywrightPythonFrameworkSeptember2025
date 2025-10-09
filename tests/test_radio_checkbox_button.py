import pytest

BASE_URL = 'https://testautomationpractice.blogspot.com/'

def test_radio_checkbox_button(page):
        page.goto(BASE_URL)
        # check the male checkbox
        radioButton = page.locator("#male")
        radioButton.check()
        assert radioButton.is_checked() is True
        page.wait_for_timeout(3000)
        print("Test Case 1 is Passed")
        
        # check the female checkbox
        radioButton1 = page.locator("#female")
        radioButton1.check()
        assert radioButton1.is_checked() is True
        page.wait_for_timeout(3000)
        print("Test Case 2 is Passed")
        
def test_select_all_checkbox(page):
        page.goto(BASE_URL)
        checkboxes = page.locator('input[type="checkbox"]')
        if checkboxes.count() >= 2:
            for index in range(checkboxes.count()):
                checkbox = checkboxes.nth(index)
                checkbox.check()
                assert checkbox.is_checked() is True
                
            
def test_selected_day(page):
    page.goto(BASE_URL)
    days = ["Monday", "Wednesday", "Friday"]
    for index in days:
        checkbox = page.get_by_label(index)
        checkbox.check()
        page.wait_for_timeout(3000)
        assert checkbox.is_checked() is True
        
