'''
Represents a visualization and uses strategy pattern for choosing
the specific graph to show.
'''

from enum import Enum
from typing import Optional

from pandas import DataFrame

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

    def show(self) -> None:
        if not self.graph:
            raise ValueError("attribute 'graph' is None, please set it with setGraph(...).")
        self.graph.plot()

    def setGraph(self, graphType: GraphType) -> None:
        if graphType == GraphType.BAR:
            self.graph = BarGraph(self.dataframe, self.y, self.groupBy)
