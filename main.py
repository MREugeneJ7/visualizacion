'''
Análisis Masivo de Datos
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

from src.dataframes_validation.numeric_dataframe import NumericDataFrame
from src.transformers.csvTransformer import CSVTransformer
from src.graphs.barGraph import BarGraph

from src.visualization import Visualization

def main() -> None:
    csvTransformer = CSVTransformer('cost-of-living.csv')
    # validatedDataframe = NumericDataFrame(csvTransformer.get())
    graphBar = BarGraph(csvTransformer.getDataFrame(), title='Foo', y='x1',
                        groupBy='city', xlabel='city', ylabel='Comida económica')
    visualization = Visualization()
    visualization.setGraph(graphBar)
    visualization.show()

if __name__ == '__main__':
    main()
