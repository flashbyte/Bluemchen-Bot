# Author: Nils Mull (mail@flash-byte.de)
# Date: 27.02.2013
import unittest
from tempPlot import tempPlot


class test_tempPlot(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getData(self):
        plot = tempPlot()
        data = plot.__getData__(10)
        self.assertGreater(len(data), 0)
