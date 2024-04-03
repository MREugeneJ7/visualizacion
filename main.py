'''
Análisis Masivo de Datos
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

from src.transformers.csvTransformer import CSVTransformer
from src.visualization import Visualization
from src.visualization import GraphType

def main() -> None:
    csvTransformer = CSVTransformer('cost-of-living.csv')
    dataframe = csvTransformer.getDataFrame()
    visualization = Visualization(dataframe.head(), y='x0', groupBy='city')
    visualization.setGraph(GraphType.BAR)
    visualization.show()

if __name__ == '__main__':
    main()
