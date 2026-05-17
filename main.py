from fastapi import FastAPI
from api.assignment_routes import router

app = FastAPI(
    title="Smart Student Assignment Tracker API"
)

@app.get("/")
def home():
    return {
        "message": "Smart Student Assignment Tracker API is running"
    }

app.include_router(router)