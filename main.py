from fastapi import FastAPI
from typing import Dict
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

app = FastAPI()

# This section reads data from json file
input_file = "test_data.json"  
with open(input_file, "r") as file:
    json_data = json.load(file)

# This is api definition which will return customer data for mentioned record
@app.get("/policy_info/{policy_no}")
async def get_screen_data(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]["Customer Info"])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/date_screen/{policy_no}")
async def date_scren(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['Date Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/vehicle_info/{policy_no}")
async def vehicle_screen(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['Vehicle Information Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/license_info/{policy_no}")
async def license_screen(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['License Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/driver_info/{policy_no}")
async def driver_scren(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['Driver Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/coverage_info/{policy_no}")
async def coverage_scren(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['Coverage Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.get("/quote_info/{policy_no}")
async def quote_scren(policy_no: int) -> Dict[str, str]:
    if int(policy_no) < len(json_data):
        json_compatible_item_data = jsonable_encoder(json_data[int(policy_no)]['Quote Screen'])
        return JSONResponse(content=json_compatible_item_data)
    else:
        return {"error": "Screen not found"}

@app.post("/login")
async def login(user: User):

    if user.password == 'sample':
        return {'message': 'login successful'}
    else:
        return {"error": "Loggin error"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
