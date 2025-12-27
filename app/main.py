from fastapi import FastAPI
from app.routes import user as user_routes   # 👈 rename
from app.core.config import APP_NAME
from app.core.database import engine
from app.models import user as user_model     # 👈 rename

# Create tables
user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include router
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.get("/info")
def info():
    return {"app": APP_NAME}
