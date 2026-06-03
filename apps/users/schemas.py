from pydantic import BaseModel
from .models import RoleEnum

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


