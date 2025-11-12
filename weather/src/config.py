from dotenv import load_dotenv
import os

load_dotenv()

USE_ROUNDED_COORDS = False
OPENWEATHER_API = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}"
    "&appid=" + str(OPENWEATHER_API) + "&lang=ru&units=metrics"
)
GEOAPIFY_API = os.getenv("GEOAPIFY_API_KEY")
GEOAPIFY_URL = (
    "https://api.geoapify.com/v1/ipinfo?&apiKey=" + str(GEOAPIFY_API)
)
