# Author: Nils Mull (mail@flash-byte.de)
# Date: 27.02.2013
import unittest
from tempPlot import tempPlot


#Todo: Create Test DB
class test_tempPlot(unittest.TestCase):
    def setUp(self):
        self.plot = tempPlot()
        pass

    def tearDown(self):
        pass

    def test_getData(self):
        data = self.plot.__getData__(10)
        self.assertGreater(len(data), 0)

    def test_getData_noData(self):
        data = self.plot.__getData__(0)
        self.assertEqual(data, None)

    def test_getData_minus(self):
        data = self.plot.__getData__(-10)
        self.assertEqual(data, None)

