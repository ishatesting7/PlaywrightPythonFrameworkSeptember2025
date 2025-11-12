from playwright.sync_api import Page

class ClassAndObjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://example.com/oops-concepts"  # Replace with the actual URL

    def navigate(self):
        self.page.goto(self.url)

    def get_page_title(self) -> str:
        return self.page.title()

    def get_page_source(self) -> str:
        return self.page.content()