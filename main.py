from fastapi import FastAPI
from routes.weather_route import router as weather_router

app = FastAPI()

app.include_router(weather_router)

