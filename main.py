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

def main() -> None:
    # _drawTopCountry()

    histogramDataframe = pd.DataFrame({
        "y": [2,3,4,2,3,4,2,3,3,2,2,2,2,2,3],
        "y2": [4,4,4,3,3,2,None,None,None,None,None,None,None,None,None,]
    })
    visualization2 = Visualization(histogramDataframe, y=['y','y2'],
                                groupBy=[-1,0, 1, 2, 3, 4, 5, 6], # the bins
                                title='Coste de comida económica por país')
    visualization2.setGraph(GraphType.HISTOGRAM)
    visualization2.show()

if __name__ == '__main__':
    main()
