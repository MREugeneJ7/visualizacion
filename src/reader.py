'''
Convert source to dataframe based on the file extension.
'''
import os
from typing import Optional

from pandas import DataFrame

from src.transformers.transformer import SourceTransformer
from src.transformers.csvTransformer import CSVTransformer

class Reader:

    def __init__(self, filePath: str):
        if not os.path.exists(filePath):
            raise OSError('Invalid file path passed to Reader.')
        if not os.path.isfile(filePath):
            raise OSError('Path passed is not a file')
        self.filePath: str = filePath
        self.transformer: Optional[SourceTransformer] = None
        self.dataframe: Optional[DataFrame] = None

    def read(self):
        _, fileExtension = os.path.splitext(self.filePath)
        if fileExtension == '.csv':
            self.transformer: Optional[SourceTransformer] = CSVTransformer(self.filePath)
            self.dataframe = self.transformer.getDataFrame()

    def getDataFrame(self):
        if self.dataframe:
            return self.dataframe
        else:
            raise ValueError('Call read() before calling getDataFrame()')