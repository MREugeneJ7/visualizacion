'''
Histogram chart visualization
'''

import inspect
from typing import Optional
from typing import Iterable
from collections.abc import Callable

from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from src.graphs.graph import Graph

class HistogramGraph(Graph):

    def __init__(self, dataframe : DataFrame, y, groupBy: Optional[Iterable],
                 title: str, xlabel: Optional[str] = None,
                 ylabel: Optional[str] = None, **args) -> None:
        super().__init__(dataframe, y)
        for i in range(1, len(groupBy)):
            if groupBy[i] < groupBy[i - 1]:
                raise ValueError('Histogram graph received a non iterable' +
                                 ' groupBy argument.')
        self._groupBy = groupBy
        self._xlabel: Optional[str] = xlabel
        self._ylabel: Optional[str] = ylabel
        self._title: str = title
        self._fig, self._ax = plt.subplots(layout='constrained')
        self._args = args

    def plot(self, callback: Optional[Callable] = None) -> None:
        # Because I want to accept any object that has [] operator implemented
        if hasattr(self._y, '__iter__') and hasattr(self._y, '__getitem__'):
            self._scatterMultigroup()
        else: 
            self._ax.hist(self._dataframe[self._groupBy], self._dataframe[self._y],
                    color ='blue', width = 0.4, **self._args)
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

    def _scatterMultigroup(self):
        colorMap = cm.get_cmap('tab10')

        for index, y in enumerate(self._y):
            self._ax.hist(self._dataframe[y], bins=self._groupBy,
                          color=colorMap(index % len(self._y)), label=y,
                          alpha=0.5, **self._args)

        # self._ax.set_xticklabels(self._dataframe[self._groupBy], rotation=75,
                                #  ha='right', fontsize='small')
        self._ax.legend(self._y)
