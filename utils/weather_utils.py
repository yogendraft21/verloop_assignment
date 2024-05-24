import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_data(city_name: str) -> dict:
    """Fetch weather data from RapidAPI."""
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    querystring = {"q": city_name}
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)

    if response.status_code == 200:
        weather_data = {
            'Weather': f"{data['current']['temp_c']} C",
            'Latitude': data['location']['lat'],
            'Longitude': data['location']['lon'],
            'City': f"{data['location']['name']} {data['location']['country']}"
        }
        return weather_data
    else:
        return None

def dict_to_xml(data: dict) -> str:
    #Convert a dictionary to an XML string.
    root = ET.Element('root')
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return ET.tostring(root, encoding='utf-8', method='xml').decode()
