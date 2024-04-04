'''
  Assignment requires the use of transformers for the data sources.
'''

import abc
from pandas import DataFrame

class SourceTransformer:

    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def getDataFrame(self) -> DataFrame:
        pass
