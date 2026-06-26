from database import supabase
from fastapi import HTTPException

def is_exist(email):
    try:
        result = supabase.table("suppliers").select("id").eq("email",email).execute()
        if result.data:
            return True
        else:
            return False
    except Exception as e :
        raise HTTPException(400,detail = str(e))

def resister_supplier(business_name,contact_phone,email,password,profile_pic:bytes):
    if not business_name or not email or not password or not contact_phone:
        raise HTTPException(400,detail="Fields are not filled")
    else:
        check_email = is_exist(email)
        if check_email == True:
            raise HTTPException(401,detail="user already exist")
        elif check_email == False:
            try :
                supabase.table("suppliers").insert({
                    "business_name":business_name,
                    "contact_phone":contact_phone,
                    "email":email,
                    "password":password
                }).execute()
                if profile_pic:
                    path = f"{email}.png"
                    supabase.storage.from_('profile_picture').upload(
                        path=path,
                        file=profile_pic,
                        file_options={"content-type": "image/png"}
                    )
                    url = supabase.storage.from_('profile_picture').get_public_url(path)
                    supabase.table("suppliers").update({
                        "profile_pic_url":url   
                    }).eq("email",email).execute()
                return {
                    "message":"account created sussefully"
                }
            except Exception as e :
                raise HTTPException(402,detail=str(e))

def signin_supplier(email,password):
    check_email = is_exist(email)
    if check_email == False:
        raise HTTPException(400,detail="user not found")
    elif check_email == True:
        try:
            responce = supabase.table("suppliers").select("id,password").eq("email",email).execute()
            passw_org = responce.data[0]["password"]
            id = responce.data[0]["id"]
            if password == passw_org:
                return {
                    "message":"Login sussefuly",
                    "id": id 
                }
            else:
                raise HTTPException(401,detail="password is incorrect")
        except Exception as e:
            raise HTTPException(402,detail=str(e))



