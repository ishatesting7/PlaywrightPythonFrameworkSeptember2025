import pytest
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_create_booking(playwright:Playwright):
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )

    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : "true",
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    start_time = time.time()
    response = request_context.post('/booking', data=payload)
    total_post_duration = time.time() - start_time

    print(f"TOTAL TIME -- {total_post_duration}")
    assert response.status == 200, f"Expected 200, got {response.status}"

    json_data = response.json()

    
    assert "bookingid" in json_data
    assert json_data["booking"]["firstname"] == "Jim"
    assert json_data["booking"]["lastname"] == "Brown"
    assert json_data["booking"]["bookingdates"]["checkin"] == "2018-01-01"

    booking_id = json_data["bookingid"]

    print(f"Booking ID Value -- {booking_id}")
    
    get_response = request_context.get(f"/booking/{booking_id}")

    assert get_response.status == 200

