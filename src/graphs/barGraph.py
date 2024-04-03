'''
Bar chart visualization
'''

from typing import Optional

from pandas import DataFrame
import matplotlib.pyplot as plt

from src.graphs.graph import Graph

class BarGraph(Graph):
    
    def __init__(self, dataframe : DataFrame, y, title, groupBy,
                xlabel: Optional[str] = None, ylabel: Optional[str] = None) -> None:
        super().__init__(dataframe, y, title)
        self._groupBy = groupBy
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self) -> None:
        # creating the bar plot
        plt.bar(self._dataframe[self._groupBy], self._dataframe[self._y], color ='maroon', 
            width = 0.4)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self._title)
        plt.show()

    def setXLabel(self, xlabel: str) -> None:
        self.xlabel = xlabel
    
    def setYLabel(self, ylabel: str) -> None:
        self.ylabel = ylabel