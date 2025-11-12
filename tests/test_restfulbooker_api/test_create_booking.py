from utils.api_client import APIClient
from utils.payload_reader import read_json

def test_create_booking():
    api = APIClient()
    payload = read_json("create_booking.json")
    response = api.create_booking(payload)
    assert response.status_code == 200
    assert "bookingid" in response.json()
