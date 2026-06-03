from sqlalchemy import Column, Integer, String, Enum
from core.database import Base
import enum

# Roles for implementing RBAC
class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index = True, nullable = False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default = RoleEnum.user)