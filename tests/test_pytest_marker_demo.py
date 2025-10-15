import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_basic_login(page:Page):
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    

@pytest.mark.smoke
def test_basic_login2(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(5000)
    
@pytest.mark.chrome    
@pytest.mark.regression
def test_basic_login2(page:Page):
    page.goto("https://www.globalsqa.com/")
    page.wait_for_timeout(5000)

@pytest.mark.skip(reason="Skipping this test for demo")
def test_basic_login3(page:Page):
    page.goto("https://www.globalsqa.com/")
    page.wait_for_timeout(5000)
    

