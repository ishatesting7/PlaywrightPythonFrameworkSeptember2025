import os
from playwright.sync_api import Page, expect

def test_file_upload_demo(page: Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    
    current_dir = os.getcwd()
    
    filepath = os.path.join(current_dir, "logs/test_run.log")
    
    filepath2 = os.path.join(current_dir, "logs/sample_log.log")
    
    page.locator('[id="filesToUpload"]').set_input_files([filepath, filepath2])
    
    page.wait_for_timeout(4000)
    