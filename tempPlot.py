# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, MinuteLocator, DateFormatter, date2num


def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class tempPlot(object):
    """docstring for tempSensot
    Class for creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

    def __get_locators(cls, period):
        if period < timedelta(days=1):
            return cls.__hour_locators(period)
        else:
            print("[ERROR]: __get_locators is not implemented for timedelta >= 1 Day")

#        days = DayLocator()  # every day
#        daysFmt = DateFormatter('%d')

    def __hour_locators(cls, period):
        if period < timedelta(hours=6):
            major_locator = HourLocator(interval=1)
            minor_locator = MinuteLocator(interval=30)
        elif period < timedelta(hours=12):
            major_locator = HourLocator(interval=3)
            minor_locator = HourLocator(interval=1)
        else:
            major_locator = HourLocator(interval=6)
            minor_locator = HourLocator()  
        fmt = DateFormatter('%H:%M')
        return major_locator, fmt, minor_locator, fmt;

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
        period = i[0]-data[0][0]

        textCelsius = u'\u00b0C'

        self.fig = plt.figure(figsize=pixelToInch(xSize, ySize, 100))
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in %s' % (textCelsius))
        ax.set_title(title)
        ax.plot(x, y)

        majorLocator, majorFmt, minorLocator, minorFormat = self.__get_locators(period)

        ax.plot_date(date2num(data[0][0]), data[0][1], '-')
        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFmt)
        ax.xaxis.set_minor_locator(minorLocator)
        textsize = 9
        # print min and max temperatur values into plot
        ax.text(0.6, 0.9, 'max = %s %s' % (maxTemp, textCelsius), va='top',
                transform=ax.transAxes, fontsize=textsize)
        ax.text(0.6, 0.1, 'min = %s %s' % (minTemp, textCelsius), va='bottom',
                transform=ax.transAxes, fontsize=textsize)

        ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
        ax.grid(True)
        self.fig.autofmt_xdate()

    def plotToFile(self, data, filename, title, xSize, ySize):
        # TODO: Error handling if no data is given
        if data is None or data == ():
            return False

        self.__plot__(data, title, xSize, ySize)

        self.fig.savefig(filename)
        return filename
