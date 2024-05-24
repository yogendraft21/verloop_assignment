from fastapi import APIRouter
from schema.weather_schema import WeatherRequest
from controller.weather_controller import get_current_weather

router = APIRouter()

@router.post("/getCurrentWeather")
async def get_current_weather_route(request: WeatherRequest):
    return await get_current_weather(request)
