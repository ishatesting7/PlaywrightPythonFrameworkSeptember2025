from playwright.sync_api import Page,expect

def test_right_click(page:Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    context_area = page.locator("#hot-spot")
    context_area.click(button="right")


def test_get_page_source(page:Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page_source = page.content()
    print(page_source)
    

def test_refresh_page(page:Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    title_before = page.title()
    print(f"Title before refresh: {title_before}")
    page.reload()
    title_after = page.title()
    print(f"Title after refresh: {title_after}")
    # expect(title_before).to_equal(title_after)
