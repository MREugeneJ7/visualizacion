'''
Bar chart visualization
'''

import inspect
from typing import Optional
from collections.abc import Callable

from pandas import DataFrame
import matplotlib.pyplot as plt

from src.graphs.graph import Graph

class BarGraph(Graph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str = None,
                xlabel: str = Optional[None], ylabel: Optional[str] = None) -> None:
        super().__init__(dataframe, y)
        self._groupBy = groupBy
        self.xlabel: Optional[str] = xlabel
        self.ylabel: Optional[str] = ylabel
        self.title: Optional[str] = title

    def plot(self, callback: Callable = lambda _: None) -> None:
        # creating the bar plot
        plt.bar(self._dataframe[self._groupBy], self._dataframe[self._y], color ='maroon', 
            width = 0.4)
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)
        if self.title:
            plt.title(self._title)

        # only pass plt if callback has a parameter for it
        paramAmount = len(inspect.signature(callback).parameters)
        if paramAmount > 0:
            callback(plt) # To allow the caller to optionally customize the plot
        else:
            callback() # To allow the caller to optionally customize the plot

        plt.show()
