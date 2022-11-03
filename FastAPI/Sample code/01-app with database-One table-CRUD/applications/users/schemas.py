from pydantic import BaseModel

class User(BaseModel):
    email:str
    password:str
    is_active: bool = False

class UpdateUser(BaseModel):
    email:str
    is_active: bool