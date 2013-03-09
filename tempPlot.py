# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
<<<<<<< HEAD

=======
import pymysql
from init import db  # , dropbox
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, date2num
>>>>>>> gfx

def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class tempPlot(object):
    """docstring for tempSensot
    Class for getting tempertur data from database, creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

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
        ax.plot(x, y)

        days = DayLocator()  # every day
        daysFmt = DateFormatter('%d')
        hours6 = HourLocator(interval=6)  # every 6 hour
        hours = HourLocator()  # every hour
        hoursFmt = DateFormatter('%H:%M')

        ax.plot_date(date2num(data[0][0]), data[0][1], '-')
        ax.xaxis.set_major_locator(hours6)
        ax.xaxis.set_major_formatter(hoursFmt)
        ax.xaxis.set_minor_locator(hours)

        ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
        ax.grid(True)
        self.fig.autofmt_xdate()

    def plotToFile(self, data, filename, title, xSize, ySize):
        self.__plot__(data, title, xSize, ySize)

        self.fig.savefig(filename)
        return filename
