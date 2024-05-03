from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn import tree
from src.graphs.graph import Graph


class DecissionTreeGraph(Graph):
    
    def __init__(self, dataframe : DataFrame, y, title: str, **args) -> None:
        super().__init__(dataframe, y, title, **args)
        self._args = args

    def plot(self) -> None:

        clf = tree.DecisionTreeClassifier(max_depth=5)
        clf = clf.fit(self._dataframe.drop(self._y), self._dataframe[self._y])

        tree.plot_tree(clf, **self._args)

        plt.set_title(self._title)

        plt.show()