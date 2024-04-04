'''
Convert source to dataframe based on the file extension.
'''
import os
from typing import Optional

from pandas import DataFrame

from src.transformers.transformer import SourceTransformer
from src.transformers.csvTransformer import CSVTransformer

class Reader:

    def __init__(self, filePath: str) -> None: 
        if not os.path.exists(filePath):
            raise OSError('Invalid file path passed to Reader.')
        if not os.path.isfile(filePath):
            raise OSError('Path passed is not a file')
        self._filePath: str = filePath

        self._dataframe: Optional[DataFrame] = None

        _, fileExtension = os.path.splitext(self._filePath)
        if fileExtension == '.csv':
            transformer: SourceTransformer = CSVTransformer(self._filePath)
            self._dataframe: Optional[DataFrame] = transformer.getDataFrame()

    def getDataFrame(self) -> DataFrame:
        if self._dataframe is None:
            raise ValueError('Call read() before calling getDataFrame()')
        return self._dataframe
