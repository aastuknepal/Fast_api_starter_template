from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm
from core.db.session import get_db
from core.auth.pw_lib import get_password_hash, verify_password
from core.auth.jwt import create_access_token, get_current_user
from users import schema, model

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model= schema.UserOut, status_code = status.HTTP_201_CREATED)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists in the database
    db_user = db.query(model.User).filter(model.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email is already registered."
        )

    # Hash the password    
    hashed_pw = get_password_hash(user.password)

    # Create new user

    new_user = model.User(
        email = user.email,
        hashed_password = hashed_pw,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schema.UserOut)
def get_current_active_user(current_user: model.User = Depends(get_current_user)):
    return current_user
