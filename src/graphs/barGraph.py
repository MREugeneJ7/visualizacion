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

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str,
                xlabel: Optional[str] = None, ylabel: Optional[str] = None) -> None:
        super().__init__(dataframe, y)
        self._groupBy = groupBy
        self._xlabel: Optional[str] = xlabel
        self._ylabel: Optional[str] = ylabel
        self._title: str = title

    def plot(self, callback: Optional[Callable] = None) -> None:
        # creating the bar plot
        plt.bar(self._dataframe[self._groupBy], self._dataframe[self._y], color ='maroon', 
            width = 0.4)
        plt.title(self._title)
        if self._xlabel is not None:
            plt.xlabel(self._xlabel)
        if self._ylabel is not None:
            plt.ylabel(self._ylabel)
        if self._title is not None:
            plt.title(self._title)

        if callback is not None:
            # only pass plt if callback has a parameter for it
            paramAmount = len(inspect.signature(callback).parameters)
            if paramAmount > 0:
                callback(plt) # To allow the caller to optionally customize the plot
            else:
                callback() # To allow the caller to optionally customize the plot

        plt.show()
