import pytest
from playwright.sync_api import Page, expect

def test_select_value_from_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    dropdown = page.locator('select[id="country"]')
    # index
    # visible text
    # option
    expect(dropdown).to_be_visible()
    dropdown.select_option("australia")
    
    selected_country = dropdown.locator("option:checked").text_content().strip()
    print(f"Selected Country --> {selected_country}")
    assert selected_country == "Australia"
    
    dropdown.select_option("brazil")
    
    selected_country = dropdown.locator("option:checked").text_content().strip()
    print(f"Selected Country --> {selected_country}")
    assert selected_country == "Brazil"
    
    dropdown.select_option(index=6)
    
    selected_country = dropdown.locator("option:checked").text_content().strip()
    print(f"Selected Country --> {selected_country}")
    assert selected_country == "Japan"
    
    all_visible_option = page.locator('select[id="country"] option').all_text_contents()
    for country_name in all_visible_option:
        select_country = country_name.strip()
        dropdown.select_option(label=select_country)
        

  
def test_select_and_validate_each_country(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    dropdown = page.locator('select#country')
    all_country_name = page.locator('select#country option')
    count_country = all_country_name.count()

    for index in range(count_country):
        option = all_country_name.nth(index)
        val = option.get_attribute('value')
        country_name = option.text_content().strip()

        if not val:
            continue

        dropdown.select_option(value=val)
        selected_value = dropdown.input_value()

        assert selected_value == val, f"Expected '{val}' but got '{selected_value}' for {country_name}"

    