'''
Análisis Masivo de Datos subject
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

import geopandas

import pandas as pd

from src.visualization import Visualization
from src.visualization import GraphType
from src.reader import Reader
from src.util.dataframeUtil import groupByAggreate, subset as ss, firstNMaxByGroup
from src.util.geographicUtils import getPoints

def _drawTopCountry(dataframe) -> None:
    visualization = Visualization(dataframe, y=['x1','x2'],
                                  groupBy='country',
                                  title='Coste de comida económica por país')
    visualization.setGraph(GraphType.BAR)
    def applyExtraConfig(_, ax):
        ax.set_xlabel('País')
        ax.set_ylabel('Coste')
        ax.xaxis.set_tick_params(labelrotation=60, length=8)
    visualization.show(post=applyExtraConfig)

def _showViolinGraph(dataframe) -> None:
    visualization = Visualization(dataframe, y='x1',
                                  groupBy='country', title='Approx. living cost',
                                  hue='country')
    visualization.setGraph(GraphType.VIOLIN)
    visualization.show()

def _showBoxplotGraph(dataframe) -> None:
    visualization = Visualization(dataframe, y='x1',
                                  groupBy='country', title='Approx. living cost')
    visualization.setGraph(GraphType.BOXPLOT)
    visualization.show()

def _showWorldMap(geodataframe) -> None:
    gdf = geopandas.GeoDataFrame(geodataframe, 
                            geometry = geodataframe['city'].map(lambda x : getPoints(x + ", Spain")), 
                            crs = "EPSG:4326")
    visualization = Visualization(dataframe=gdf, y='x54',
                                  groupBy='artificial_total', title='GDP each year per country')
    visualization.setGraph(GraphType.MAP)
    visualization.show()

def main() -> None:
    readerDf1 = Reader("cost-of-living_v2.csv", dropna = True)
    dataframeGCL = readerDf1.getDataFrame()
    readerDf2 = Reader("GDP.csv", 2)
    dataframeGDP = readerDf2.getDataFrame()

    # calculate top 20 countries with the most expensive economic type food
    dataframeWithOnlyTopCountries = firstNMaxByGroup(dataframeGCL, 20, 'country', 'x1')
    # _drawTopCountry(dataframeWithOnlyTopCountries)

    dataframeGCL = dataframeGCL[dataframeGCL["country"] == "Spain"]
    subset = ss(dataframeGCL, "city", "x1", "x28", "x49", "x54")
    newCol = map(lambda x : x[1] * 365 + x[2] * 365 + x[3] * 12, subset.values)
    subset["artificial_total"] = list(newCol)
    subset['x54'] = subset['x54'].map(lambda x : x * 12)
    onlyInterestingColumns = subset[['city', 'artificial_total',
                                          'x54']].dropna()

    visualization = Visualization(dataframe=onlyInterestingColumns[['x54', 'artificial_total']], y='x54',
                                  groupBy='artificial_total', title='Cost of living vs Expected salary')
    visualization.setGraph(GraphType.REGRESSION_SCATTER)
    visualization.show()
    visualization.getOutput()

    # gdf = geopandas.GeoDataFrame(onlyInterestingColumns, 
    #                              geometry = onlyInterestingColumns['Country Name'].map(lambda x : get_coordinates(x)), 
    #                              crs = "EPSG:4326")
    # visualization2 = Visualization(gdf, "2022", None, None)
    # visualization2.setGraph(GraphType.MAP)
    # visualization2.show()

    # TODO:
    # Change representation to better visualize GDP.
    # Refactor all dataframe things into a UtilityClass/Wrapper
    # temporal solution to distance being too big to display
    # head(23) doesn't work, head(22) works
    
    _showWorldMap(onlyInterestingColumns)
    # _showBoxplotGraph(subset.head(15))
    # _showViolinGraph(subset.head(12))

    # countryAmount = len(pd.unique(dataframeGCL['country']))
    # visualizationCluster = Visualization(dataframeGCL, y=['x1', 'x28', 'x49'],
    #                                      groupBy='country', title='Cluster groups',
    #                                      clusteringColumns=['x1', 'x28', 'x49'],
    #                                      n_clusters=countryAmount)
    # visualizationCluster.setGraph(GraphType.CLUSTERING_SCATTER)
    # visualizationCluster.show()

if __name__ == '__main__':
    main()
