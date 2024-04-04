'''
  All graphs have this in common
'''

from typing import Optional
from collections.abc import Callable

import abc

class Graph(metaclass = abc.ABCMeta):

    def __init__(self, dataframe, y, title: str = None) -> None:
        self._dataframe = dataframe
        self._y = y
        self._title: Optional[str] = title

    @abc.abstractmethod
    def plot(callback: Optional[Callable] = None) -> None:
        pass