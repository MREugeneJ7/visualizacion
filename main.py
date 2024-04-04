'''
Análisis Masivo de Datos subject
Universidad de La Laguna
Visualization Assignment
'''

__authors__ = ["Marcos Barrios", "Eugenio Gonzalez"]
__date__ = "2024/04/03"

from src.visualization import Visualization
from src.visualization import GraphType
from src.reader import Reader

def main() -> None:
    reader = Reader('cost-of-living.csv')
    reader.read()
    dataframe = reader.getDataFrame()
    visualization = Visualization(dataframe.head(), y='x1', groupBy='city', title='Test')
    visualization.setGraph(GraphType.BAR)
    visualization.show()

if __name__ == '__main__':
    main()
