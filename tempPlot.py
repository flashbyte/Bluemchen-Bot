# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, date2num


def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class tempPlot(object):
    """docstring for tempSensot
    Class for creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

    def __plot__(self, data, title, xSize=500, ySize=400):
        x = []
        y = []
        maxTemp = -275
        minTemp = 1000
        for i in data:
            x.append(i[0])
            y.append(i[1])
            if i[1] < minTemp:
                minTemp = i[1]
            if i[1] > maxTemp:
                maxTemp = i[1]

        textCelsius = u'\u00b0C'

        self.fig = plt.figure(figsize=pixelToInch(xSize, ySize, 100))
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in %s' %(textCelsius))
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
        textsize = 9
        # print min and max temperatur values into plot
        ax.text(0.6, 0.9, 'max = %s %s' %(maxTemp, textCelsius), va='top', transform=ax.transAxes, fontsize=textsize)
        ax.text(0.6, 0.1, 'min = %s %s' %(minTemp, textCelsius), va='bottom', transform=ax.transAxes, fontsize=textsize)

        ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
        ax.grid(True)
        self.fig.autofmt_xdate()

    def plotToFile(self, data, filename, title, xSize, ySize):
        # TODO: Error handling if no data is given
        if data == None or data == ():
            return False

        self.__plot__(data, title, xSize, ySize)

        self.fig.savefig(filename)
        return filename
