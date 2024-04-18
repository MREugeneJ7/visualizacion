
from pandas import DataFrame


def subset(input : DataFrame, *columns : str) -> DataFrame:
    return input[list(columns)]

def groupByAggreate(input : DataFrame, column: str, method : str) -> DataFrame:
    return input.groupby(column).aggregate(method)