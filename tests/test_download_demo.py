import os

from playwright.sync_api import Page, expect

def test_file_download_demo(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    
    with page.expect_download() as download_info:
        page.locator("//a[text()='testing.pdf']").click()
    download = download_info.value
    print(download.path)
    
    page.wait_for_timeout(4000)
    
    working_dir_path = os.getcwd()
    final_path = os.path.join(working_dir_path,"reports/demo.pdf")
    download.save_as(final_path)
    