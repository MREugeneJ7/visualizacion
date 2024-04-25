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

from src.graphs.machinelearning.decisionTreeGraph import DecissionTreeGraph
from src.graphs.graph import Graph
from src.graphs.barGraph import BarGraph
from src.graphs.lineGraph import LineGraph
from src.graphs.scatterGraph import ScatterGraph
from src.graphs.histogramGraph import HistogramGraph
from src.graphs.violinGraph import ViolinGraph

class GraphType(Enum):
    BAR = 0,
    LINE = 1,
    SCATTER = 2,
    HISTOGRAM = 3,
    DECISION_TREE = 4,
    VIOLIN = 5,

class Visualization:

    def __init__(self, dataframe: DataFrame, y, groupBy, title: str) -> None:
        self._graph: Optional[Graph] = None
        self._dataframe: DataFrame = dataframe
        self._y = y
        self._groupBy = groupBy
        self._title: str = title

    # pre is called before plotting the graph, while post is called
    # after plotting the graph
    def show(self, pre: Optional[Callable] = None,
            post: Optional[Callable] = None) -> None:
        if not self._graph:
            raise ValueError("attribute 'graph' is None, please set it with setGraph(...).")

        if pre is not None:
            # only pass plt if callback has a parameter for it
            paramAmount = len(inspect.signature(pre).parameters)
            if paramAmount > 0:
                pre(plt)
            else:
                pre()

        if post is not None:
            self._graph.plot(post)
        else:
            self._graph.plot()

    def setGraph(self, graphType: GraphType) -> None:
        if graphType == GraphType.BAR:
            self._graph = BarGraph(self._dataframe, self._y, self._groupBy,
                                   self._title)
        if graphType == GraphType.LINE:
            self._graph = LineGraph(self._dataframe, self._y, self._groupBy,
                                    self._title)
        if graphType == GraphType.SCATTER:
            self._graph = ScatterGraph(self._dataframe, self._y, self._groupBy,
                                       self._title)
        if graphType == GraphType.HISTOGRAM:
            self._graph = HistogramGraph(self._dataframe, self._y, self._groupBy,
                                         self._title)
        if graphType == GraphType.DECISION_TREE:
            self._graph = DecissionTreeGraph(self._dataframe, self._y,
                                             self._title)
        if graphType == GraphType.VIOLIN:
            self._graph = ViolinGraph(self._dataframe, self._y, self._groupBy,
                                      self._title)
