from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/users')
async def get_users():
    try:
        users = conn.test.users.find()
        dict_users = usersEntity(users)
    except Exception as error:
        print(error)
        
    return dict_users 

