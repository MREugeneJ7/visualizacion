'''
  Because visualizations require specific dataframes.
  For example, if a visualization is meant for continuous data,
  then a dataframe with strings would not be valid.
'''

import pandas as pd
from pandas import DataFrame

# WIP

class NumericDataframe():

    def __init__(self, filePath: str) -> None:
        self.data = pd.read_csv(filePath)

    def get(self) -> DataFrame:
        return self.data
