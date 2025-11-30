from coordinates import get_gps_coordinates
from weather_api_service import get_weather, get_forecast
from weather_formatter import format_weather, format_forecast

def main():
    coordinates = get_gps_coordinates()
    weather = get_weather(coordinates)
    print(format_weather(weather))
    print("\n")
    forecast = get_forecast(coordinates)
    print(format_forecast(forecast))

if __name__ == "__main__":
    main()