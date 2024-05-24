### Requirements

- Python 3.6+
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd weather_app
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the environment variables:

Create a .env file in the root directory of the project and add your RapidAPI key:

RAPIDAPI_KEY=<your_rapidapi_key>
Run the FastAPI server:uvicorn main:app --reload
The server will start running on http://127.0.0.1:8000 by default.

Make a POST request to the /getCurrentWeather endpoint with the following JSON payload:

json
{
    "city": "<city_name>",
    "output_format": "<json_or_xml>"
}
Replace <city_name> with the name of the city for which you want to retrieve the weather data, and <json_or_xml> with either "json" or "xml" depending on the desired output format.

Receive the weather data response in the specified format (JSON or XML).

Method: POST

URL: /getCurrentWeather

Request Body:

json
Copy code
{
    "city": "<city_name>",
    "output_format": "<json_or_xml>"
}
city: Name of the city for which weather data is requested.
output_format: Desired output format, either "json" or "xml".
Response:

JSON Format:

json
Copy code
{
    "Weather": "<weather_info>",
    "Latitude": "<latitude>",
    "Longitude": "<longitude>",
    "City": "<city_name>"
}
XML Format:

xml
Copy code
<?xml version="1.0" encoding="UTF-8" ?>
<root>
    <Weather><weather_info></Weather>
    <Latitude><latitude></Latitude>
    <Longitude><longitude></Longitude>
    <City><city_name></City>
</root>
Replace placeholders <city_name>, <json_or_xml>, <weather_info>, <latitude>, and <longitude> with appropriate values when making requests.
