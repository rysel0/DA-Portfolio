"""Format ouput for weather"""
from datetime import datetime
from weather_api_service import Weather, Forecast


def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"Время и дата: {datetime.now()}\n"
            f"Город: {weather.city}\n"
            f"Температура: {weather.temperature}°C\n"
            f"Описание погоды: {weather.weather_type.value}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")


def format_forecast(forecast_list: list[Forecast]) -> str:
    """Formats forecast data in string"""
    result = "Прогноз погоды на 5 дней:\n" + "=" * 50 + "\n"
    for forecast in forecast_list:
        result += (f"Дата и время: {forecast.date.strftime('%Y-%m-%d %H:%M')}\n"
                   f"Температура: {forecast.temperature}°C\n"
                   f"Описание погоды: {forecast.weather_type.value}\n"
                   + "-" * 50 + "\n")
    return result


if __name__ == "__main__":
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-03 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-03 20:25:00"),
        city="Москва"
    )))
