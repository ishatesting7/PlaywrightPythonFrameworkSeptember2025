import pytest
from playwright.sync_api import Page, expect


def select_subject(page,subject):
    auto_suggestion = page.locator("div.subjects-auto-complete__option")
    index = 0
    while index < auto_suggestion.count():
        if auto_suggestion.nth(index).inner_text().strip() == subject:
            auto_suggestion.nth(index).click()
            break
        index += 1
    page.wait_for_timeout(30000)
    
# class="subjects-auto-complete__option css-yt9ioa-option"
def test_select_autosuggestion_dropdown(page: Page):
    
    page.goto('https://demoqa.com/automation-practice-form')
    page.wait_for_timeout(15000)
    subject_input = page.locator("#subjectsInput")
    subject_input.fill("Hi")
    page.get_by_text("History", exact=True).click()
    # select_subject(page,"History")
    
    