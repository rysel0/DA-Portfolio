"""Module get coordinates by IP Address"""
from typing import NamedTuple

import requests

import config
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns currentt coordinates using {http://api.geopify.com}"""
    url = config.GEOAPIFY_URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        #latitude, longitude = data['lat'], data['lon']
        latitude, longitude = data['location']['latitude'], data['location']['longitude']
        return _round_cordinates(Coordinates(latitude=latitude, longitude=longitude))
    
    except requests.RequestException as e:
        raise CantGetCoordinates(f"Ошибка при запросе: {e}") from e
    

def _round_cordinates(coordinates: Coordinates) -> Coordinates:
    if config.USE_ROUNDED_COORDS:
        return Coordinates(*map(lambda c: round(c, 1), coordinates))
    else:
        return coordinates


if __name__ == '__main__':
    coordinates = get_gps_coordinates()

    print(coordinates.latitude)
    print(coordinates.longitude)
