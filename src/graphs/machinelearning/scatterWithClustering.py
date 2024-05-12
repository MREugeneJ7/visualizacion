

from collections.abc import Callable
from typing import Any, Optional
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.cluster import AgglomerativeClustering
from src.graphs.scatterGraph import ScatterGraph


class ScatterWithClustering(ScatterGraph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str,
                xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                **args) -> None:
        super().__init__(dataframe, y, groupBy, title, xlabel, ylabel, **args)
        self._model = self.agglomerativeClustering() 

    def agglomerativeClustering(self):
        #TODO: change distance/n_clusters
        clustering = AgglomerativeClustering(distance_threshold=0, linkage=self._args["clustering_type"], n_clusters=None)
        return clustering.fit(self._dataframe)
    
    def plot(self, callback: Callable[..., Any] | None = None) -> None:
        self._args['c'] = self._model.labels_
        del self._args['clustering_type']
        super().preplot(callback)
        plt.show()

