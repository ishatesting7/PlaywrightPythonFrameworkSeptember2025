import pytest
from playwright.sync_api import sync_playwright

def test_screenshot_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/python/")
        page.screenshot(path="screenshot.png")
        page.screenshot(path="screenshot_full.png", full_page=True)
        page.screenshot(path="screenshot_element.png", clip=page.locator("[class='getStarted_Sjon']").bounding_box())
        page.screenshot(path="screenshot_quality.jpg", quality=80, type="jpeg")
        page.screenshot(path="screenshot_omit_background.png", omit_background=True)
        browser.close()
        