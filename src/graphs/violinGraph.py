'''
Violin chart visualization
'''

import inspect
from typing import Optional
from typing import Iterable
from collections.abc import Callable

from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

from src.graphs.graph import Graph

class ViolinGraph(Graph):

    def __init__(self, dataframe : DataFrame, y : str | Iterable[str],
                 groupBy: Optional[Iterable], title: str,
                 hue: str | Iterable[str] = None, xlabel: Optional[str] = None,
                 ylabel: Optional[str] = None) -> None:
        super().__init__(dataframe, y)
        self._groupBy : Optional[Iterable] = groupBy
        self._xlabel: Optional[str] = xlabel
        self._ylabel: Optional[str] = ylabel
        self._title: str = title
        self._hue : str | Iterable[str] = hue

    def plot(self, callback: Optional[Callable] = None) -> None:
        sns.set_theme()
        g : sns.FacetGrid = sns.catplot(data=self._dataframe, kind='violin',
                                        x=self._groupBy, y=self._y,
                                        hue=self._groupBy, split=True,
                                        dropna=True)

        plt.title(self._title)
        if self._xlabel is not None:
            g.set_xlabel(self._xlabel)
        if self._ylabel is not None:
            g.set_ylabel(self._ylabel)

        if callback is not None:
            # only pass plt if callback has a parameter for it
            paramAmount = len(inspect.signature(callback).parameters)
            if paramAmount > 0:
                # To allow the caller to optionally customize the plot
                callback(g)
            else:
                callback() # To allow the caller to optionally customize the plot

        plt.show()