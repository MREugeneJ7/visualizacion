
from typing import List

import numpy as np
from collections.abc import Callable
from typing import Any, Optional
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.cluster import AgglomerativeClustering
from src.graphs.scatterGraph import ScatterGraph

class ScatterWithClustering(ScatterGraph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str, 
                linkage : Optional[str] = "ward", distance_threshold : Optional[float] = None,
                n_clusters: Optional[int] = None, xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                clusteringColumns: List[str] = None, **args) -> None:
        super().__init__(dataframe, y, groupBy, title, xlabel, ylabel, **args)
        self._linkage= linkage
        self._distance_threshold = distance_threshold

        if clusteringColumns != None and (
                hasattr(clusteringColumns, '__iter__') and hasattr(clusteringColumns, '__getitem__')):
            self._dataframe = self._dataframe[clusteringColumns]

        self._model = self.agglomerativeClustering()

    def agglomerativeClustering(self):
        clustering = AgglomerativeClustering(distance_threshold=self._distance_threshold, linkage=self._linkage, n_clusters=self._n_clusters)
        return clustering.fit(self._dataframe)

    def plot(self, callback: Callable[..., Any] | None = None) -> None:
        self._args['c'] = self._model.labels_
        super().preplot(callback)
        plt.show()
