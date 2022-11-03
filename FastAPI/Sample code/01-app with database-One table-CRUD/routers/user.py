from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/user",
    tags=["app1"]
)



users =[]

@router.get('')
async def get_users():
    return users

    
@router.post('')
async def createt_user(user):
    users.append(user)
    return {user}