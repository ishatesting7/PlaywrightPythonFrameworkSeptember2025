from playwright.sync_api import Page, expect    

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def refresh_page(self):
        self.page.reload()

    def get_page_source(self) -> str:
        return self.page.content()

    def assert_title_contains(self, text: str):
        assert text in self.get_title(), f"Expected '{text}' to be in page title '{self.get_title()}'"