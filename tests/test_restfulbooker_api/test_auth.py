from utils.api_client import APIClient

def test_create_auth_token():
    api = APIClient()
    response = api.create_auth_token()
    assert response.status_code == 200
    assert "token" in response.json()
    
