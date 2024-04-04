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

def main() -> None:
    print('Reading csv file.')
    reader = Reader('cost-of-living.csv')
    dataframe = reader.getDataFrame()

    # calculate top 20 countries with the most expensive economic type food
    topGroups: pd.Series[np.float64] = dataframe.groupby('country')['x1'].max().nlargest(20)
    dataframeTopCountries = dataframe[dataframe['country'].isin(topGroups.index)]
    dataframeTopCountriesSorted = dataframeTopCountries.sort_values(by='x1', ascending=False)

    print('Visualising the result.')
    visualization = Visualization(dataframeTopCountriesSorted, y='x1', groupBy='country',
                                  title='Coste de comida económica por país')
    visualization.setGraph(GraphType.BAR)
    def applyExtraConfig(plt):
        plt.xlabel('País')
        plt.ylabel('Coste')
        plt.xticks(rotation=60, ha='right', fontsize=8)
    visualization.show(post=applyExtraConfig)

if __name__ == '__main__':
    main()
