# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt


def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class tempPlot(object):
    """docstring for tempSensot
    Class for getting tempertur data from database, creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

    # FIXME: X and Y Size / Resolution error
    def __plot__(self, data, title, xSize=500, ySize=400):
        x = []
        y = []
        for i in data:
            x.append(i[0])
            y.append(i[1])
        self.fig = plt.figure(figsize=pixelToInch(xSize, ySize, 100))
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in C')
        ax.set_title(title)
        # TODO: Bad date fomate
        ax.plot(x, y)

    def plotToFile(self, data, title, xSize, ySize):
        self.__plot__(data, title, xSize, ySize)
        filename = tempfile.mkstemp(suffix='.png')[1]  # Don't need this!
        self.fig.savefig(filename)
        return filename
