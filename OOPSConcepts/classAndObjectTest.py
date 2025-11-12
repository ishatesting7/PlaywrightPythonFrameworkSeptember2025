from OOPSConcepts.classAndObject import ClassAndObjectPage

def test_valid_login(page):
    class_page = ClassAndObjectPage(page)
    class_page.navigate()
    
    title = class_page.get_page_title()
    source = class_page.get_page_source()
    
    assert "OOPS Concepts" in title
    assert "<h1>OOPS Concepts</h1>" in source