from fastapi import FastAPI, APIRouter
from users.router import router as users_router

app = FastAPI(
    title = "Your Title",
    description= "Your description",
    version = "1.0.0"
)

# Create an APIRouter for v1 endpoints
api_v1_router = APIRouter(prefix="/api/v1")

# Include individual app routers into the v1 router
api_v1_router.include_router(users_router)

# Include the v1 router into the main FastAPI app
app.include_router(api_v1_router)

# Simple api check
@app.get("/")
def read_root():
    return {"status": "System is online", 
    "Message": "Welcome to the api"}