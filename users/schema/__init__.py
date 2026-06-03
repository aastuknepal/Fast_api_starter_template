from pydantic import BaseModel
from users.model import RoleEnum

# Input scheme: What user can send

class UserCreate(BaseModel):
    email : str
    password : str
    role : RoleEnum = RoleEnum.user  # Defaults to user if nothing provided

class UserOut(BaseModel):
    id: int
    email: str
    role: RoleEnum

    class Config:
        from_attributes = True 

class Token(BaseModel):
    access_token: str
    token_type: str

