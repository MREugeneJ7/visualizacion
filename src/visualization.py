'''
Represents a visualization and uses strategy pattern for choosing
the specific graph to show.
'''

import inspect
from enum import Enum
from typing import Optional
from collections.abc import Callable

from pandas import DataFrame
import matplotlib.pyplot as plt

from src.graphs.graph import Graph
from src.graphs.barGraph import BarGraph

class GraphType(Enum):
    BAR = 0

class Visualization:

    def __init__(self, dataframe: DataFrame, y, groupBy) -> None:
        self.graph: Optional[Graph] = None
        self.dataframe: DataFrame = dataframe
        self.y = y
        self.groupBy = groupBy

    def show(self, callback: Callable = lambda _: None) -> None:
        if not self.graph:
            raise ValueError("attribute 'graph' is None, please set it with setGraph(...).")

        # only pass plt if callback has a parameter for it
        paramAmount = len(inspect.signature(callback).parameters)
        if paramAmount > 0:
            callback(plt) # To allow the caller to optionally customize the plot
        else:
            callback() # To allow the caller to optionally customize the plot

        self.graph.plot()

    def setGraph(self, graphType: GraphType) -> None:
        if graphType == GraphType.BAR:
            self.graph = BarGraph(self.dataframe, self.y, self.groupBy)
