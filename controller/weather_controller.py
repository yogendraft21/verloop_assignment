from fastapi import HTTPException, Response
from utils.weather_utils import get_weather_data, dict_to_xml
from schema.weather_schema import WeatherRequest

async def get_current_weather(request: WeatherRequest) -> Response:
    #Handle the /getCurrentWeather endpoint.
    city = request.city
    output_format = request.output_format

    if not city:
        raise HTTPException(status_code=400, detail="City name is required")

    weather_data = get_weather_data(city)

    if not weather_data:
        raise HTTPException(status_code=500, detail="Could not fetch weather data")

    if output_format.lower() == 'xml':
        xml_response = dict_to_xml(weather_data)
        return Response(content=xml_response, media_type="application/xml")
    else:
        return weather_data
