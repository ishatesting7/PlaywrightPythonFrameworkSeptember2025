from utils.api_client import ApiClient

def test_create_booking(playwright):
    request_context = playwright.request.new_context()

    api_client = ApiClient(request_context)

    payload = json.dumps({
         "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : true,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    })
    
    with allure.step("Send Post Request for Create Booking"):
        response = api_client.create_booking(payload)
        assert response.status == 200, f"Unexpected status":{response.status}"

        