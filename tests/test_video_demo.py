import pytest
from playwright.sync_api import sync_playwright
import os
def test_video_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 800, "height": 600})
        
        page = context.new_page()
        page.goto("https://playwright.dev/python/")
        page.wait_for_timeout(2000)  # Wait for 2 seconds to capture some
        page.click("text=GET STARTED")
        page.wait_for_timeout(2000)  # Wait for 2 seconds to capture some
        context.close()
        browser.close()
        