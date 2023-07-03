import json
import random
from faker import Faker

# Initialize Faker generator
fake = Faker()

# Generate Customer Info data
def generate_customer_info():
    cust_name = fake.name()
    address = fake.address()
    contact_no = fake.phone_number()
    age = random.randint(18, 65)
    gender = random.choice(["Male", "Female"])
    id_proof = fake.random_element(["Aadhaar Card", "Driver's License", "Passport"])
    driving_license = fake.random_number(digits=12)
    passport = fake.random_number(digits=12)
    
    customer_info = {
        "cust_name": cust_name,
        "address": address,
        "contact_no": contact_no,
        "age": age,
        "gender": gender,
        "id_proof": id_proof,
        "Driving License": driving_license,
        "passport": passport
    }
    return customer_info

# Generate Date screen data
def generate_date_screen():
    from_date = fake.date_between(start_date="-30d", end_date="+30d").strftime("%Y-%m-%d")
    duration = random.randint(1, 5)
    
    date_screen = {
        "from_date": from_date,
        "duration_in_years": duration
    }
    return date_screen

# Generate Vehicle Information screen data
def generate_vehicle_info_screen():
    registered_owner = fake.name()
    regn_date = fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")
    color = fake.color_name()
    fuel = random.choice(["Petrol", "Diesel", "Electric"])
    vehicle_class = fake.random_element(["Hatchback", "Sedan", "SUV"])
    body_type = fake.random_element(["SUV", "Coupe", "Convertible"])
    manufacturer = fake.random_element(["Toyota", "Honda", "Ford", "Hyundai"])
    chassis_no = fake.random_number(digits=17)
    engine_no = fake.random_number(digits=15)
    model_no = fake.random_number(digits=10)
    hypothecated_to = fake.name()
    mfg_date = fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
    seat_capacity = random.randint(2, 7)
    no_of_cyc = random.randint(2, 4)
    regd_validity = fake.date_between(start_date="today", end_date="+1y").strftime("%Y-%m-%d")
    tax_paid_up_to = fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d")
    
    vehicle_info_screen = {
        "registered_owner": registered_owner,
        "regn_date": regn_date,
        "color": color,
        "fuel": fuel,
        "vehicle_class": vehicle_class,
        "body_type": body_type,
        "manufacturer": manufacturer,
        "chassis_no": chassis_no,
        "engine_no": engine_no,
        "model_no": model_no,
        "hypothecated_to": hypothecated_to,
        "mfg_date": mfg_date,
        "seat_capacity": seat_capacity,
        "no_of_cyc": no_of_cyc,
        "regd_validity": regd_validity,
        "tax_paid_up_to": tax_paid_up_to
    }
    return vehicle_info_screen

# Generate License screen data
def generate_license_screen():
    name = fake.name()
    address = fake.address()
    license_no = fake.random_number(digits=10)
    license_type = fake.random_element(["LMV", "MCWG", "HMV"])
    date_of_issue = fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")
    valid_till = fake.date_between(start_date="today", end_date="+5y").strftime("%Y-%m-%d")
    
    license_screen = {
        "name": name,
        "address": address,
        "license_no": license_no,
        "license_type": license_type,
        "date_of_issue": date_of_issue,
        "valid_till": valid_till
    }
    return license_screen

# Generate Driver screen data
def generate_driver_screen():
    driver_name = fake.name()
    age = random.randint(25, 60)
    experience = random.randint(1, 20)
    conviction = fake.random_element(["No", "Yes"])
    
    driver_screen = {
        "driver_name": driver_name,
        "age": age,
        "experience": experience,
        "conviction": conviction
    }
    return driver_screen

# Generate Coverage screen data
def generate_coverage_screen():
    collision = random.choice([True, False])
    comprehensive = random.choice([True, False])
    third_party = random.choice([True, False])
    
    coverage_screen = {
        "collision": collision,
        "comprehensive": comprehensive,
        "third_party": third_party
    }
    return coverage_screen

# Generate Quote screen data
def generate_quote_screen():
    collision_premium = random.randint(1000, 5000)
    comprehensive_premium = random.randint(2000, 8000)
    third_party_premium = random.randint(500, 2000)
    
    quote_screen = {
        "collision_premium": collision_premium,
        "comprehensive_premium": comprehensive_premium,
        "third_party_premium": third_party_premium
    }
    return quote_screen

# Generate test data
def generate_test_data():
    test_data = {
        "Customer Info": generate_customer_info(),
        "Date Screen": generate_date_screen(),
        "Vehicle Information Screen": generate_vehicle_info_screen(),
        "License Screen": generate_license_screen(),
        "Driver Screen": generate_driver_screen(),
        "Coverage Screen": generate_coverage_screen(),
        "Quote Screen": generate_quote_screen()
    }
    return test_data

# Store data in a JSON file
output_file = "test_data.json"
n = 10
with open(output_file, "w") as file:
    file.write("[")
    for i in range(n):
        json.dump(generate_test_data(), file, indent=4)
        if i < n-1:
            file.write(",")
    file.write("]")

print(f"Test data generated and stored in {output_file}")
