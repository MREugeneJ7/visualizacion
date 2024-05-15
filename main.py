'''
Análisis Masivo de Datos subject
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

import pandas as pd
import numpy as np
import geopandas

from shapely import Point
import pycountry
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

from src.visualization import Visualization
from src.visualization import GraphType
from src.reader import Reader
from src.util.dataframeUtil import groupByAggreate, subset as ss
from src.util.geographicUtils import get_coordinates

def _drawTopCountry() -> None:
    print('Reading csv file.')
    reader = Reader('cost-of-living.csv')
    dataframe = reader.getDataFrame()

    # calculate top 20 countries with the most expensive economic type food
    topX1: pd.Series[np.float64] = dataframe.groupby('country')['x1'].transform('max')
    dataframeWithOnlyTopCountries = (
        dataframe[dataframe['x1'] == topX1]
        .drop_duplicates(subset=['country', 'x1'])
        .nlargest(20, 'x1')
    )

    
    print('Visualising the result.')
    visualization = Visualization(dataframeWithOnlyTopCountries, y=['x1','x2'],
                                  groupBy='country',
                                  title='Coste de comida económica por país')
    visualization.setGraph(GraphType.BAR)
    def applyExtraConfig(_, ax):
        ax.set_xlabel('País')
        ax.set_ylabel('Coste')
        ax.xaxis.set_tick_params(labelrotation=60, length=8)
    visualization.show(post=applyExtraConfig)

# WIP, I am gonna make the GPD-artificial_total scatter
def _showViolinGraph(dataframe) -> None:
    visualization = Visualization(dataframe, y='x1',
                                  groupBy='country', title='Approx. living cost',
                                  hue='country')
    visualization.setGraph(GraphType.VIOLIN)
    visualization.show()

def _showBoxplotGraph(dataframe) -> None:
    visualization = Visualization(dataframe, y=['x1','x28'],
                                  groupBy='country', title='Approx. living cost')
    visualization.setGraph(GraphType.BOXPLOT)
    visualization.show()


def main() -> None:
    # _drawTopCountry()

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
    maxAttempts = 10
    def getPoints(country, attempts=0):
        try:
            country_obj = pycountry.countries.get(name=country)
            geolocator = Nominatim(user_agent="amd-project-ull")
            location = geolocator.geocode(country_obj.name)
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
    print("Finished geodataframe")
    visualization = Visualization(dataframe=gdf, y='2022',
                                  groupBy='artificial_total', title='GDP each year per country')
    visualization.setGraph(GraphType.MAP)
    print("Entering show()")
    visualization.show()
    print("Finished show()")

    # visualization2 = Visualization(gdf, "2022", None, None)
    # visualization2.setGraph(GraphType.MAP)
    # visualization2.show()

    # TODO:
    # Change representation to better visualize GDP.
    # Refactor all dataframe things into a UtilityClass/Wrapper

    # _showBoxplotGraph(subset.head(15))
    # _showViolinGraph(subset.head(12))

if __name__ == '__main__':
    main()
