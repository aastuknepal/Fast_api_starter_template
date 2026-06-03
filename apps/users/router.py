from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import get_password_hash
from . import schemas, models

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model= schemas.UserOut, status_code = status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists in the database
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email is already registered."
        )

    # Hash the password    
    hashed_pw = get_password_hash(user.password)

    # Create new user

    new_user = models.User(
        email = user.email,
        hashed_password = hashed_pw,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

