'''
  Assignment requires the use of transformers for the data sources.
  This reads .csv files into a valid DataFrame.
'''

import pandas as pd
from pandas import DataFrame

from src.transformers.transformer import SourceTransformer

class CSVTransformer(SourceTransformer):

    def __init__(self, filePath: str, header:int, dropna: bool) -> None:
        if(dropna):
          self._data = pd.read_csv(filePath, header=header).dropna()
        else:
          self._data = pd.read_csv(filePath, header=header)
    def getDataFrame(self) -> DataFrame:
        return self._data
