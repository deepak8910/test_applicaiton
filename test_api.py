import pytest
import requests
import json
import logging as log

# Configure logging
log.basicConfig(filename='test_logs.log', level=log.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


base_url = "http://0.0.0.0:8000"
input_file = "test_data.json"  # Replace with the path to your generated JSON file
with open(input_file, "r") as file:
    json_data = json.load(file)

record_count = len(json_data)



@pytest.fixture(scope="module")
def api_client():
    return requests.Session()

def send_post_payload(url, api_client, payload):
    response = api_client.post(url, json=payload)
    # Validate the response
    assert response.status_code == 200, f"Status Code: {response.status_code}"
    return response.json()


def send_payload(url, api_client):   
    headers = {
        "Content-Type": "application/json"
    }
    response = api_client.get(url, headers=headers)

    # Validate the response
    assert response.status_code == 200, f"Failed to send payload to {screen}. Status Code: {response.status_code}"

    return response.json()


@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_customer_info(api_client, policy_number):
    url = f"{base_url}/policy_info/{policy_number}"
    result = send_payload(url, api_client)
    validate_customer(result)

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_negative_customer_info(api_client, policy_number):
    url = f"{base_url}/policy_info/{policy_number}"
    result = send_payload(url, api_client)
    # Validate the result
    validate_customer(result)

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_date_screen(api_client, policy_number):
    url = f"{base_url}/date_screen/{policy_number}"   
    result = send_payload(url, api_client)
    # Validate the result
    validate_date(result)
    assert 'from_date' in result

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_vehicle_screen(api_client, policy_number):
    url = f"{base_url}/vehicle_info/{policy_number}"   
    result = send_payload(url, api_client)
    # Validate the result
    validate_vehicle_info(result)
    assert 'registered_owner' in result

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_license_screen(api_client, policy_number):
    url = f"{base_url}/license_info/{policy_number}"   
    result = send_payload(url, api_client)
    validate_license(result)
    assert 'license_no' in result

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_driver_screen(api_client, policy_number):
    url = f"{base_url}/driver_info/{policy_number}"   
    result = send_payload(url, api_client)
    # Validate the result
    validate_driver(result)
    assert 'conviction' in result

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_coverage_screen(api_client, policy_number):
    url = f"{base_url}/coverage_info/{policy_number}"   
    result = send_payload(url, api_client)
    # Validate the result
    validate_coverage(result)
    assert 'collision' in result

@pytest.mark.parametrize("policy_number", list(range(record_count)))
def test_quote_screen(api_client, policy_number):
    url = f"{base_url}/quote_info/{policy_number}"   
    result = send_payload(url, api_client)
    # Validate the result
    validate_quote(result)
    assert 'collision_premium' in result

def test_login_api(api_client):
	url = f'{base_url}/login'
	payload = {
		'username': 'deepak',
		'password': 'sample'
	}
	result  = send_post_payload(url, api_client, payload)

def test_failed_login_api(api_client):
	url = f'{base_url}/login'
	payload = {
		'username': 'deepak',
		'password': 'sample2'
	}
	result  = send_post_payload(url, api_client, payload)
	assert result['error'] == 'Loggin error'


def validate_customer(result):
	assert 'cust_name' in result
	assert 'address' in result
	assert 'contact_no' in result
	assert 'age' in result
	assert 'gender' in result
	assert 'id_proof' in result
	assert 'Driving License' in result
	assert 'passport' in result
	log.info(f"Validation successful for customer. Result: {result}")

def validate_date(result):
	assert "from_date" in result
	assert "duration_in_years" in result
	log.info(f"Validation successful for dates. Result: {result}")

def validate_vehicle_info(result):
    assert "registered_owner" in result
    assert "regn_date" in result
    assert "color" in result
    assert "fuel" in result
    assert "vehicle_class" in result
    assert "body_type" in result
    assert "manufacturer" in result
    assert "chassis_no" in result
    assert "engine_no" in result
    assert "model_no" in result
    assert "hypothecated_to" in result
    assert "mfg_date" in result
    assert "seat_capacity" in result
    assert "no_of_cyc" in result
    assert "regd_validity" in result
    assert "tax_paid_up_to"  in result
    log.info(f"Validation successful for vehicle information. Result: {result}")

def validate_license(result):
    assert "name"  in result
    assert "address"  in result
    assert "license_no"  in result
    assert "license_type"  in result
    assert "date_of_issue"  in result
    assert "valid_till"  in result
    log.info(f"Validation successful for license. Result: {result}")

def validate_driver(result):
    assert "driver_name" in result
    assert "age" in result
    assert "experience" in result
    assert "conviction" in result
    log.info(f"Validation successful for driver. Result: {result}")

def validate_coverage(result):
    assert "collision" in result
    assert "comprehensive" in result
    assert "third_party" in result
    log.info(f"Validation successful for coverage. Result: {result}")

def validate_quote(result):
    assert "collision_premium" in result
    assert "comprehensive_premium" in result
    assert "third_party_premium" in result
    log.info(f"Validation successful for quote. Result: {result}")




