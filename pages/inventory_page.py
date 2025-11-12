from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.inventory_items = page.locator(".inventory_item")
        self.cart_button = page.locator(".shopping_cart_link")
        self.filter_dropdown = page.locator(".product_sort_container")
        self.souce_backpage = page.locator("//div[text()='Sauce Labs Backpack']")
        self.add_to_cart_souce_backpage = page.locator('[data-test="add-to-cart"]')
        
    def is_loaded(self) -> bool:
        return self.inventory_items.is_visible()
    
    def add_product_to_cart(self):
        self.souce_backpage.click()
        self.add_to_cart_souce_backpage.click()
        self.cart_button.click()
