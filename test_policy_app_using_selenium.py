from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox WebDriver
options = Options()
options.headless = True  # Run in headless mode (without opening browser window)
driver = webdriver.Firefox(options=options)

# Load the JSON data
json_data = {
    "Customer_Info": {
        "cust_name": "Lindsay Smith",
        "address": "6575 Lisa Ports\nNew Joel, FL 62142",
        "contact_no": "988-610-9831",
        "age": 56,
        "gender": "Female",
        "id_proof": "Passport",
        "Driving License": 380615447270,
        "passport": 482480279603
    },
    "Date": {
        "from_date": "2023-07-03",
        "duration_in_years": 1
    },
    "Vehicle_Information": {
        "registered_owner": "John Williamson",
        "regn_date": "2018-11-18",
        "color": "SaddleBrown",
        "fuel": "Electric",
        "vehicle_class": "Sedan",
        "body_type": "Coupe",
        "manufacturer": "Honda",
        "chassis_no": 17489919096130298,
        "engine_no": 58232413227195,
        "model_no": 2988008033,
        "hypothecated_to": "Daniel Williams",
        "mfg_date": "2016-12-28",
        "seat_capacity": 5,
        "no_of_cyc": 3,
        "regd_validity": "2023-11-29",
        "tax_paid_up_to": "2023-04-26"
    },
    "License_info": {
        "name": "Benjamin Briggs",
        "address": "02361 Lindsey Villages Suite 867\nKingmouth, DC 40100",
        "license_no": 7040634378,
        "license_type": "LMV",
        "date_of_issue": "2018-10-17",
        "valid_till": "2024-12-25"
    },
    "driverInfo": {
        "driver_name": "John Tran",
        "age": 54,
        "experience": 11,
        "conviction": "Yes"
    },
    "coverage": {
        "collision": True,
        "comprehensive": False,
        "third_party": False
    },
    "quote": {
        "collision_premium": 3215,
        "comprehensive_premium": 3707,
        "third_party_premium": 1204
    }
}

# Open the application URL
driver.get("http://application_url/Customer_Info")

# Function to fill data for each screen and submit
def fill_screen_data(screen_data):
    for field, value in screen_data.items():
        field_element = driver.find_element_by_id(field)
        field_element.send_keys(str(value))
    time.sleep(1)  # Wait for the form to be filled (adjust as needed)
    submit_button = driver.find_element_by_id("submit_button")
    submit_button.click()
    time.sleep(1)  # Wait for the next page to load (adjust as needed)

# Fill and submit data for each screen
fill_screen_data(json_data["Customer_Info"])
actual_url = driver.current_url
if actual_url == "http://application_url/Date":
    fill_screen_data(json_data["Date"])
else:
    assert False, "Page not found Error"
if actual_url == "http://application_url/Vehicle_Information":
    fill_screen_data(json_data["Vehicle_Information"])
else:
    assert False, "Page not found Error"
if actual_url == "http://application_url/License_info":
    fill_screen_data(json_data["License_info"])
else:
    assert False, "Page not found Error"
if actual_url == "http://application_url/coverage":
    fill_screen_data(json_data["coverage"])
else:
    assert False, "Page not found Error"
if actual_url == "http://application_url/quote":
    fill_screen_data(json_data["quote"])
    if actual_url == "http://application_url/payment":
        assert True, "Successfully filled policy application."
else:
    assert False, "Page not found Error"

# Close the browser
driver.quit()
