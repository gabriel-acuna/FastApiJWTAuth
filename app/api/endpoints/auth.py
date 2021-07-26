from fastapi import APIRouter, Body

from app.schemas.auth import  UserLoginSchema, UserSchema
from app.api.auth.auth_handler import signJWT

router = APIRouter()

users = []


def check_user(data: UserLoginSchema.UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@router.post("/signup")
async def create_user(user: UserSchema.UserSchema = Body(...)):
    users.append(user) 
    return signJWT(user.email)
    

@router.post("/login")
async def user_login(user: UserLoginSchema.UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }