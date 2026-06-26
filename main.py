
from login import signin_supplier
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from login import resister_supplier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 🔓 Allows any application or mobile bundle to connect
    allow_credentials=False,  # ✅ FIXED: Must be False when allow_origins is ["*"]
    allow_methods=["*"],      # 🔓 Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],      # 🔓 Allows all custom header types
)
@app.post("/login")
async def resister_suppliers(business_name:str,contact_phone:str,email:str,password:str,profile_pic:UploadFile=File(...)):
    image_bytes = await profile_pic.read()
    return resister_supplier(business_name,contact_phone,email,password,image_bytes)
@app.post("/signin")
async def signin_suppliers(email:str,password:str):
    return signin_supplier(email,password)

