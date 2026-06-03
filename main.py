from fastapi import FastAPI
from apps.users.router import router as users_router

app = FastAPI(
    title = "Your Title",
    description= "Your description",
    version = "1.0.0"
)

app.include_router(users_router)

# Simple api check

@app.get("/")
def read_root():
    return {"status": "System is online", 
    "Message": "Welcome to the api"}