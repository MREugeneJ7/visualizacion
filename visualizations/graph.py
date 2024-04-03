import abc

class Graph(metaclass = abc.ABCMeta):
    
    def __init__(self, dataframe, y, title) -> None:
        self._dataframe = dataframe
        self._y = y
        self._title = title
    
    @abc.abstractmethod
    def plot() -> None:
        pass