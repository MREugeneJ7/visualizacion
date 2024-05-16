

from collections.abc import Callable
from typing import Any, Optional
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.cluster import DBSCAN
from src.graphs.scatterGraph import ScatterGraph


class ScatterWithOutliers(ScatterGraph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str, 
                epsilon : Optional[float] = 0.5, min_samples : Optional[int] = 5, 
                xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                **args) -> None:
        super().__init__(dataframe, y, groupBy, title, xlabel, ylabel, **args)
        self._epsilon= epsilon
        self._min_samples = min_samples
        self._model = self.agglomerativeClustering() 

    def agglomerativeClustering(self):
        clustering = DBSCAN(eps=self._epsilon, min_samples=self._min_samples)
        return clustering.fit(self._dataframe)
    
    def plot(self, callback: Callable[..., Any] | None = None) -> None:
        self._args['color'] = list(map(lambda l : "red" if l == -1 else "blue", self._model.labels_))
        super().preplot(callback)
        plt.show()

