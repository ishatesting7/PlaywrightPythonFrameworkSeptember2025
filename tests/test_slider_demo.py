from playwright.sync_api import Page, expect

def test_slider_demo(page: Page):
    page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    
    slider_loc = page.locator("div.sliderContainer input")
    slider_point = page.locator("#range")
    range_max = '4'
    
    slider_loc.click()
    
    while True:
        if slider_point.inner_text() == range_max:
            break
        slider_loc.press("ArrowRight")
        page.wait_for_timeout(1000)
        
        if slider_point.inner_text() == '5':
            break
        
        page.wait_for_timeout(5000)
        
        

def test_slider_jquery_demo(page:Page):
    page.goto("https://jqueryui.com/slider/")
    frame = page.frame_locator(".demo-frame") 
    slider = frame.locator("#slider span")
    slider.click()
    for _ in range(50):
        slider.press("ArrowRight")
        page.wait_for_timeout(1000)
        if slider.get_attribute("style") == "left: 100%;":
            break
    
    page.wait_for_timeout(4000)
    