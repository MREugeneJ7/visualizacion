
import numpy as np
from pandas import DataFrame, Series

def subset(input : DataFrame, *columns : str) -> DataFrame:
    return input[list(columns)]

def groupByAggreate(input : DataFrame, column: str, method : str) -> DataFrame:
    return input.groupby(column).aggregate(method)

def firstNMaxByGroup(dataframe, n: int, group: str, valuesColumn: str):
    topX1: Series[np.float64] = dataframe.groupby(group)[valuesColumn].transform('max')
    return (
        dataframe[dataframe[valuesColumn] == topX1]
        .drop_duplicates(subset=[group, valuesColumn])
        .nlargest(n, valuesColumn)
    )