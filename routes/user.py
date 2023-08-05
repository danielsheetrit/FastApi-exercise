from fastapi import APIRouter
from models.user import User
from config.db import test_db
from schemas.user import userEntity, usersEntity

user = APIRouter()
users_col = test_db['users']

@user.get('/users')
async def get_users():
    try:
        users = users_col.find()
        dict_users = usersEntity(users)
    except Exception as error:
        print(error)
    return dict_users 

@user.post('/users')
async def create_user(user: User):
    res = users_col.insert_one(dict(user))
    
    if res.acknowledged:
        return 'success'
