"""Program for get weather from OpenWeatherAPI"""
from typing import NamedTuple, TypeAlias
from datetime import datetime
from enum import Enum
import json
from json.decoder import JSONDecodeError

import requests

from exceptions import ApiServiceError
from coordinates import Coordinates
import config

Celsius: TypeAlias = int

class WeatherType(Enum):
    """Class includes avaliable weather types from OpenWeather"""
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    FOG = 'Туман'
    CLOUDS = 'Облачно'


class Weather(NamedTuple):
    """Key components of weather"""
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


class Forecast(NamedTuple):
    """Key components of forecast"""
    temperature: Celsius
    weather_type: WeatherType
    date: datetime


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        lattitude=coordinates.latitude, longitude=coordinates.longitude)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(lattitude: float, longitude: float):
    url = config.OPENWEATHER_URL.format(lat = lattitude, lon = longitude)
    try:
        return requests.get(url = url, timeout = 5).content
    except Exception as exc:
        raise ApiServiceError from exc


def _parse_openweather_response(weather_response: bytes) -> Weather:
    try:
        openweather_dict = json.loads(weather_response)
    except JSONDecodeError as exc:
        raise ApiServiceError from exc
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise = _parse_sun_time(openweather_dict, 'sunrise'),
        sunset = _parse_sun_time(openweather_dict, 'sunset'),
        city=_parse_city(openweather_dict)
        )


def _parse_temperature(weather_dict: dict) -> Celsius:
    return round(weather_dict['main']['temp'] -273.15)


def _parse_weather_type(weather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(weather_dict['weather'][0]['id'])
    except (IndexError, KeyError) as exc:
        raise ApiServiceError from exc
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }

    for _id in weather_types:
        if weather_type_id.startswith(_id):
            return weather_types[_id]
    raise ApiServiceError


def _parse_sun_time(weather_dict: dict, suntype: str) -> datetime:
    return datetime.fromtimestamp(weather_dict['sys'][suntype])


def _parse_city(weather_dict: dict) -> str:
    return weather_dict['name']


def get_forecast(coordinates: Coordinates) -> list[Forecast]:
    """Requests weather forecast in OpenWeather API and returns it"""
    openweather_response = _get_openweather_forecast_response(
        lattitude=coordinates.latitude, longitude=coordinates.longitude)
    forecast = _parse_openweather_forecast_response(openweather_response)
    return forecast


def _get_openweather_forecast_response(lattitude: float, longitude: float):
    url = config.OPENWEATHER_FORECAST_URL.format(lat=lattitude, lon=longitude)
    try:
        return requests.get(url=url, timeout=5).content
    except Exception as exc:
        raise ApiServiceError from exc


def _parse_openweather_forecast_response(forecast_response: bytes) -> list[Forecast]:
    try:
        openweather_dict = json.loads(forecast_response)
    except JSONDecodeError as exc:
        raise ApiServiceError from exc
    
    forecast_list = []
    for item in openweather_dict.get('list', []):
        forecast_list.append(Forecast(
            temperature=_parse_temperature(item),
            weather_type=_parse_weather_type(item),
            date=datetime.fromtimestamp(item['dt'])
        ))
    return forecast_list


if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=55.7967, longitude=49.1913)))
