import geopandas
from shapely import Point, distance
import pycountry
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
import contextily as cx
from matplotlib import pyplot as plt
from src.reader import Reader
from src.util.dataframeUtil import groupByAggreate, subset as ss

readerDf1 = Reader("cost-of-living_v2.csv", dropna = True)
dataframeGCL = readerDf1.getDataFrame()
readerDf2 = Reader("GDP.csv", 2)
dataframeGDP = readerDf2.getDataFrame()

subset = ss(dataframeGCL, "country", "x1", "x28", "x49")
subsetByCountry = groupByAggreate(subset,"country", "mean")

newCol = map(lambda x : x[0] * 365 + x[1] * 365 + x[2] * 12 ,subsetByCountry.values)
subsetByCountry["artificial_total"] = list(newCol)

superjoin = dataframeGDP.join(subsetByCountry, on="Country Name")

# # Get x1, x28, x49, 2022
onlyInterestingColumns = (superjoin[['Country Name', 'artificial_total',
                                        '2022']].dropna())
onlyInterestingColumns = onlyInterestingColumns.drop(index=35)
# head(50) doesnt work
# head(30) doesnt work
# head(25) doesnt work
onlyInterestingColumns = onlyInterestingColumns.head(2)

maxAttempts = 10
foo = True
bar = True
def getPoints(country, attempts=0):
    global foo
    global bar
    try:
        country_obj = pycountry.countries.get(name=country)
        geolocator = Nominatim(user_agent="amd-project-ull")
        location = geolocator.geocode(country_obj.name)
        if foo == True:
            foo = False
            return Point(-107.99171, 61.06669)
        if bar == True:
            bar = False
            return Point(134.755, -24.7761086)
        return Point(location.longitude, location.latitude)
    except AttributeError:
        print(f"attribute error for {country}")
        return None
    except GeocoderTimedOut:
        if attempts < maxAttempts:
            print (f"retry for {country}")
            return getPoints(country, attempts=attempts + 1)
        print(f"None for {country}")
        return None

gdf = geopandas.GeoDataFrame(onlyInterestingColumns, 
                        geometry = onlyInterestingColumns['Country Name'].map(lambda x : getPoints(x)), 
                        crs = "EPSG:4326")
# farthestRightPoint = None
# farthestDistance = 0
# canadaPoint = Point(-107.99171, 61.06669)
# for index, row in gdf.iterrows():
#     point = row['geometry']
#     if farthestRightPoint == None or distance(point, canadaPoint) > farthestDistance:
#         farthestRightPoint = point
#         farthestDistance = distance(point, canadaPoint)
# print(farthestRightPoint)
# print(farthestDistance)

print(gdf)
ax = gdf.plot('2022', legend = True)
cx.add_basemap(ax, crs=gdf.crs, zoom=10)
plt.show()

