from graph import Graph
from pandas import DataFrame
import matplotlib.pyplot as plt

class BarGraph(Graph):
    
    def __init__(self, dataframe : DataFrame, y, title, groupBy) -> None:
        super().__init__(dataframe, y, title)
        self._groupBy = groupBy
        
    def plot(self) -> None:
        # creating the bar plot
        plt.bar(self._dataframe[self._groupBy], self._dataframe[self._y], color ='maroon', 
            width = 0.4)
        columns = self._dataframe.columns
        plt.xlabel(columns[self._groupBy])
        plt.ylabel(columns[self._y])
        plt.title(self._title)
        plt.show()