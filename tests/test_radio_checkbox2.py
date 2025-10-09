import pytest
from playwright.sync_api import Page, expect

def test_select_all_checkboxes(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()
    print(f"Found {count} checkboxes")
    for i in range(count):
        cb = checkboxes.nth(i)
        if not cb.is_checked():
            cb.check()
    for i in range(count):
        assert checkboxes.nth(i).is_checked()
