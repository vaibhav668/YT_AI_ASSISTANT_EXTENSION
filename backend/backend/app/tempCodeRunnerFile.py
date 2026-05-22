from fastapi import FastAPI
from app.routes.youtube_routes import router as youtube_router
app=FastAPI()

app.include_router(youtube_router)
@app.get("/")
def home():
    return {"message": "YouTube AI Backend Running"}


