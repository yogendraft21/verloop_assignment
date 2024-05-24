from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str
    output_format: str
