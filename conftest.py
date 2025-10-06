import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # set True for headless
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page() # New tab is opened
    yield page
    page.close()