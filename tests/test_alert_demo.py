from playwright.sync_api import Page

def test_alert_demo(page: Page):
    page.goto("https://sweetalert2.github.io/")
    show_success_message = page.locator("//button[@aria-label='Show SweetAlert2 success message']")
    show_success_message.click()
    
    alert_msg = page.locator("#swal2-title")
    alert_msg_text = alert_msg.inner_text()
    print(f"Alert message text: {alert_msg_text}")
    assert alert_msg_text == "Good job!"
    
    page.locator("button", has_text="OK").click()
    
    assert not alert_msg.is_visible(),"The Alert is No Longer Visible"
    