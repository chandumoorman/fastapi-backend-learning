from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.deps import get_db
from app.core.security import hash_password, verify_password

router = APIRouter(prefix="/users", tags=["Users"])

# STEP 5: SIGNUP API
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


# STEP 6: LOGIN API  👇👇👇
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        return {"error": "Invalid credentials"}

    return {"message": "Login successful"}
