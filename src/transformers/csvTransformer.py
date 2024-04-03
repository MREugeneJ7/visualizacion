'''
  Assignment requires the use of transformers for the data sources.
  This reads .csv files into a valid DataFrame.
'''

import pandas as pd
from pandas import DataFrame

from src.transformers.transformer import SourceTransformer

class CSVTransformer(SourceTransformer):

    def __init__(self, filePath: str) -> None:
        self.data = pd.read_csv(filePath)

    def getDataFrame(self) -> DataFrame:
        return self.data
