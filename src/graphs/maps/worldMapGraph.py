import geopandas
from matplotlib import pyplot as plt

from src.graphs.graph import Graph

class WorldMapGraph(Graph):

    def __init__(self, dataframe : geopandas.GeoDataFrame, y, title: str,
                 **args) -> None:
        super().__init__(dataframe, y, title)
        self._args = args

    # self._y is the column to use for coloring
    def plot(self) -> None:
        self._dataframe.plot(self._y, legend = True, **self._args)
        plt.show()