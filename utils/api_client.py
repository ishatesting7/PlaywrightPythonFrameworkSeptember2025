import requests
from utils import config

class APIClient:
    def __init__(self):
        self.base_url = config.BASEURL
        self.session = requests.Session()
        self.token = None
    
    def create_auth_token(self):
        url = f"{self.base_url}/auth"
        payload = {"username": config.USERNAME, "password": config.PASSWORD}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        self.token = response.json().get("token")
        return response
    
    def get_booking(self, booking_id):
        return self.session.get(f"{self.base_url}/booking/{booking_id}")
    
    def create_booking(self, payload):
        return self.session.post(f"{self.base_url}/booking",json=payload)
    
    def update_booking(self, booking_id, payload):
        headers = {"Cookie":f"token = {self.token}"}
        return self.session.put(f"{self.base_url}/booking/{booking_id}",json=payload,headers=headers)

    def partial_update_booking(self, booking_id, payload):
        headers = {"Cookie":f"token = {self.token}"}
        return self.session.patch(f"{self.base_url}/booking/{booking_id}",json=payload,headers=headers)

    def delete_booking(self, booking_id):
        headers = {"Cookie":f"token = {self.token}"}
        return self.session.delete(f"{self.base_url}/booking/{booking_id}",headers=headers)
