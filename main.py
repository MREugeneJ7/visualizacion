'''
Análisis Masivo de Datos subject
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

import pandas as pd
import numpy as np

from src.visualization import Visualization
from src.visualization import GraphType
from src.reader import Reader
from src.util.dataframeUtil import groupByAggreate, subset as ss

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
    # onlyInterestingColumns = (superjoin[['Country Name', 'artificial_total',
    #                                       '2022']].dropna())

    # visualization = Visualization(onlyInterestingColumns, y='artificial_total',
    #                               groupBy='2022', title='GDP per country ' +
    #                               'vs approx. living cost')
    # visualization.setGraph(GraphType.SCATTER)
    # visualization.show()

    _showViolinGraph(subset.head(12))
    # _showBoxplotGraph(subset.head(15))

if __name__ == '__main__':
    main()
