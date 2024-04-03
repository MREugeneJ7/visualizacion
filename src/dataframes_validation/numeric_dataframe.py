'''
  Because graph require specific dataframes.
  For example, if a visualization is meant for continuous data,
  then a dataframe with strings would not be valid.
'''

import pandas as pd
from pandas import DataFrame

class NumericDataFrame():

    def __init__(self, dataframe: DataFrame) -> None:
        for columnName, series in dataframe.items():
            pd.to_numeric(series, errors='raise')
        self.dataframe = dataframe

    def get(self) -> DataFrame:
        return self.dataframe
