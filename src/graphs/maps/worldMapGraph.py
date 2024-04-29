import geopandas
from matplotlib import pyplot as plt

from src.graphs.graph import Graph

class WorldMapGraph(Graph):
    
    def __init__(self, dataframe : geopandas.GeoDataFrame, y, title: str) -> None:
        super().__init__(dataframe, y, title)

    def plot(self) -> None:
        self._dataframe.plot(self._y, legend = True)
        plt.show()