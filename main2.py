from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

class CustomerInfo(BaseModel):
    cust_name: str
    address: str
    contact_no: str
    age: int
    gender: str
    id_proof: str
    DrivingLicense: str
    passport: str

app = FastAPI()

@app.post("/send-customer-data")
async def submitCustomerInfo(customer_info: CustomerInfo):
    payload = {
        "Customer Info": customer_info.dict()
    }

    try:
        print(payload)  # Corrected variable name
        with open("data.json", "a") as file:
            json.dump(payload, file, indent=4)
            file.write(",\n")  # Add newline character after each payload
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to write payload to JSON file.")
    return {"message": "Payload written to JSON file."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)