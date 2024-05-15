from geopy.geocoders import Nominatim
import pycountry
from shapely.geometry import Point
from geopy.exc import GeocoderTimedOut

maxAttempts = 10
def getPoints(country, attempts=0):
    try:
        country_obj = pycountry.countries.get(name=country)
        geolocator = Nominatim(user_agent="amd-project-ull")
        location = geolocator.geocode(country_obj.name)
        return Point(location.longitude, location.latitude)
    except AttributeError:
        print(f"Openstreemaps attribute error for {country}")
        return None
    except GeocoderTimedOut:
        if attempts < maxAttempts:
            print (f"query retry for {country}")
            return getPoints(country, attempts=attempts + 1)
        print(f"None for {country}")
        return None