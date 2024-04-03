'''
Testing barGraph class
'''

import unittest

import pandas as pd

from src.graphs.barGraph import BarGraph

class BarGraphTestCase(unittest.TestCase):

    def test_Callback(self):
        dataframe = pd.DataFrame({ 'y':[3, 6, 1, 2], 'groupBy':[1, 2, 3, 4] })
        barGraph = BarGraph(dataframe, 'y', 'groupBy')
        def extraConfig(plt):
            plt.xlabel('tw')
        barGraph.plot(extraConfig)
