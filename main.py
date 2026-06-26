
from login import signin_supplier
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from login import resister_supplier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 🔓 Allows any website/domain to access this API
    allow_credentials=True,   # Note: Set to False if using allow_origins=["*"] with strict browser cookies
    allow_methods=["*"],      # 🔓 Allows all HTTP actions (POST, GET, OPTIONS, PUT, DELETE)
    allow_headers=["*"],      # 🔓 Allows any custom headers to be passed through
)

@app.post("/login")
async def resister_suppliers(business_name:str,contact_phone:str,email:str,password:str,profile_pic:UploadFile=File(...)):
    image_bytes = await profile_pic.read()
    return resister_supplier(business_name,contact_phone,email,password,image_bytes)
@app.post("/signin")
async def signin_suppliers(email:str,password:str):
    return signin_supplier(email,password)

