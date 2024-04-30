from geopy.geocoders import Nominatim
import pycountry
from shapely.geometry import Point

def get_coordinates(country):
    try:
        country_obj = pycountry.countries.get(name=country)
        geolocator = Nominatim(user_agent="visualizacion")
        location = geolocator.geocode(country_obj.name)
        return Point(location.latitude, location.longitude)
    except AttributeError:
        return Point(0,0)