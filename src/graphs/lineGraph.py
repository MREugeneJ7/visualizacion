'''
Line chart visualization
'''

import inspect
from typing import Optional
from collections.abc import Callable

from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from src.graphs.graph import Graph

class LineGraph(Graph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str,
                xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                **args) -> None:
        super().__init__(dataframe, y)
        self._groupBy = groupBy
        self._xlabel: Optional[str] = xlabel
        self._ylabel: Optional[str] = ylabel
        self._title: str = title
        self._fig, self._ax = plt.subplots(layout='constrained')
        self._args = args

    def plot(self, callback: Optional[Callable] = None) -> None:
        # creating the line plot
        if hasattr(self._y, '__iter__') and hasattr(self._y, '__getitem__'):
            self._lineMultigroup()
        else: 
            self._ax.plot(self._dataframe[self._groupBy],
                          self._dataframe[self._y], **self._args)

        self._ax.set_title(self._title)
        if self._xlabel is not None:
            self._ax.set_xlabel(self._xlabel)
        if self._ylabel is not None:
            self._ax.set_ylabel(self._ylabel)

        if callback is not None:
            # only pass plt if callback has a parameter for it
            paramAmount = len(inspect.signature(callback).parameters)
            if paramAmount > 0:
                # To allow the caller to optionally customize the plot
                callback(self._fig, self._ax)
            else:
                callback() # To allow the caller to optionally customize the plot

        plt.show()

    def _lineMultigroup(self):
        x = np.arange(len(self._dataframe[self._groupBy]))

        colorMap = cm.get_cmap('tab10')

        multiplier = 0
        for index, y in enumerate(self._y):
            self._ax.plot(x, self._dataframe[y],
                          color=colorMap(index % len(self._y)), label=y,
                          **self._args)

        self._ax.set_xticks(x, self._dataframe[self._groupBy])
        self._ax.set_xticklabels(self._dataframe[self._groupBy], rotation=75,
                                 ha='right', fontsize='small')
        self._ax.legend(self._y)
