import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def test_create_booking(playwright:Playwright):
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )

    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    response = request_context.post('/booking', data=payload)

    assert response.status == 200, f"Expected 200, got {response.status}"
