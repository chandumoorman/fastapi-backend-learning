from fastapi import FastAPI
from app.routes import user
from app.core.config import APP_NAME

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/info")
def info():
    return {"app": APP_NAME}
