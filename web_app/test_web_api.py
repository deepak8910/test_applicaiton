import requests
from pydantic import BaseModel
import pytest

# Define the payload
false = False
true = True

base_url = "http://0.0.0.0:8000"

@pytest.fixture(scope="module")
def api_client():
    return requests.Session()

def send_post_payload(url, api_client, payload):
    response = api_client.post(url, json=payload)
    # Validate the response
    assert response.status_code == 200, f"Status Code: {response.status_code}"
    return response.json()


class Payload(BaseModel):
    data: dict

payload = {
        "cust_name": "Christina Harris",
        "address": "1910 Robertson Coves Suite 930\nSouth Dawn, NM 78769",
        "contact_no": "975.722.9875x08857",
        "age": 19,
        "gender": "Male",
        "id_proof": "Driver's License",
        "DrivingLicense": '159083682841',
        "passport": '37821335321' }

# Set the headers for the request
headers = {
    "Content-Type": "application/json"
}

def test_login_api(api_client):
    url = f'{base_url}/send-customer-data'
    result  = send_post_payload(url, api_client, payload)
    print(result)
