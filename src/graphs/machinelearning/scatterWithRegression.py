

import numpy as np
from collections.abc import Callable
from typing import Any, Optional
from matplotlib import pyplot as plt
from pandas import DataFrame, Series
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from src.graphs.scatterGraph import ScatterGraph


class ScatterWithRegressionGraph(ScatterGraph):

    def __init__(self, dataframe : DataFrame, y, groupBy, title: str,
                xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                **args) -> None:
        super().__init__(dataframe, y, groupBy, title, xlabel, ylabel, **args)
        self._regression_x, self._predicted_y = self.predict_y()

    def predict_y(self):
        X_train, X_test, y_train, y_test = train_test_split(self._dataframe[self._groupBy], self._dataframe[self._y], test_size=0.33, random_state=42)
        regr = linear_model.LinearRegression()
        regr.fit(DataFrame(X_train), DataFrame(y_train))
        self._regr = regr
        return X_test, regr.predict(DataFrame(X_test))
    
    def plot(self, callback: Callable[..., Any] | None = None) -> None:
        colorMask = self.getOutput()
        super().preplot(callback, c=colorMask)
        self._ax.plot(self._regression_x, self._predicted_y, color="red",
                      linewidth=3, **self._args)
        plt.show()

    # get the real values that are higher than the predicted values
    def getOutput(self):
        predicted = self._regr.predict(DataFrame(self._dataframe[self._groupBy])).flatten()
        real = self._dataframe[self._y].values
        result = DataFrame({
            'a': predicted,
            'b': real,
        })
        colorMask = np.where(result['b'] >= result['a'], 'green', 'blue')
        return colorMask
