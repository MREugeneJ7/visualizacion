'''
Represents a visualization and uses strategy pattern for choosing
the specific graph to show.
'''

from visualizations.graph import Graph

class Visualization:
    
    def __init__(self) -> None:
        self.graph = None
    
    def show(self) -> None:
        if not self.graph:
            raise ValueError("attribute 'graph' is None, please set it with setGraph(...).")
        self.graph.plot()

    def setGraph(self, graph: Graph) -> None:
        self.graph = graph
