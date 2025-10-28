from playwright.sync_api import Page

def test_iframe_demo(page: Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    # Switch to the top frame
    main_f = page.main_frame
    
    for child_frame in main_f.child_frames:
        print(child_frame.name)
    
    top_frame = page.main_frame.child_frames[0]
    bottom_frame = page.main_frame.child_frames[1]
    
    left_top_frame = top_frame.child_frames[0]
    middle_top_frame = top_frame.child_frames[1]
    right_top_frame = top_frame.child_frames[2]
    
    print(left_top_frame.locator("body").inner_text())
    print(middle_top_frame.locator("body").inner_text())
    print(right_top_frame.locator("body").inner_text())