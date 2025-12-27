from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    username: str 
    email: str 



@app.post("/users")
def create_user(user: User):
    return{
        "username": user.username,
        "email": user.email
    }