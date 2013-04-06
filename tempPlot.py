# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, MinuteLocator, \
    WeekdayLocator, MonthLocator, DateFormatter, date2num, MO

# constant for unicode degree symbol
TEXT_CELSIUS = u'\u00b0'


def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class TempPlot(object):
    """docstring for tempSensot
    Class for creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

    @classmethod
    def __set_locators(cls, period, ax):
        if period < timedelta(days=1):
            majorLocator, majorFmt, minorLocator, minorFmt = \
                cls.__hour_locators(period)
        elif period < timedelta(weeks=2):
            majorLocator, majorFmt, minorLocator, minorFmt = \
                cls.__day_locators(period)
        else:
            majorLocator, majorFmt, minorLocator, minorFmt = \
                cls.__month_locators(period)
        # set locators on axis
        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFmt)
        ax.xaxis.set_minor_locator(minorLocator)

    @classmethod
    def __month_locators(cls, period):
        if period < timedelta(weeks=12):
            majorLocator = WeekdayLocator(byweekday=MO, interval=1)
            majorFmt = DateFormatter('%d.%m')
            minorLocator = DayLocator(interval=1)
            minorFmt = DateFormatter('%d')
        else:
            majorLocator = Monthlocator(interval=1)
            majorFmt = DateFormatter('%m.%Y')
            minorLocator = WeekdayLocator(byweekday=MO, interval=1)
            minorFmt = DateFormatter('%d')
        return majorLocator, majorFmt, minorLocator, minorFmt

    @classmethod
    def __day_locators(cls, period):
        if period < timedelta(days=3):
            majorLocator = DayLocator(interval=1)
            minorLocator = HourLocator(interval=6)
            minorFmt = DateFormatter('%H:%M')
        elif period < timedelta(days=7):
            majorLocator = DayLocator(interval=1)
            minorLocator = HourLocator(interval=12)
            minorFmt = DateFormatter('%H:%M')
        else:
            majorLocator = DayLocator(interval=7)
            minorLocator = DayLocator(interval=1)
            minorFmt = DateFormatter('%d.%m')
        majorFmt = DateFormatter('%d.%m')
        return majorLocator, majorFmt, minorLocator, minorFmt

    @classmethod
    def __hour_locators(cls, period):
        if period < timedelta(hours=2):
            majorLocator = HourLocator(interval=1)
            minorLocator = MinuteLocator(interval=30)
        if period < timedelta(hours=6):
            majorLocator = HourLocator(interval=1)
            minorLocator = MinuteLocator(interval=30)
        elif period < timedelta(hours=12):
            majorLocator = HourLocator(interval=3)
            minorLocator = HourLocator(interval=1)
        else:
            majorLocator = HourLocator(interval=6)
            minorLocator = HourLocator()
        fmt = DateFormatter('%H:%M')
        return majorLocator, fmt, minorLocator, fmt

#    @deprecated
    def __plot__(self, data, title, xSize=500, ySize=400):
        self.fig = self.__plot(data, title, ('Zeit', 'Temperatur in %sC' % 
                                             TEXT_CELSIUS), (xSize, ySize))

    @classmethod
    def __plot(cls, data, title, axisLabels, dimension):
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

        fig = plt.figure(figsize=pixelToInch(dimension[0], dimension[1], 100))
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.set_xlabel(axisLabels[0])
        ax.set_ylabel(axisLabels[1])
        ax.plot(x, y)
        ax.plot_date(date2num(data[0][0]), data[0][1], '-')
        # set xaxis locators
        cls.__set_locators(period, ax)

        textsize = 9
        # print min and max temperatur values into plot
        ax.text(0.6, 0.9, 'max = %s %sC' % (maxTemp, TEXT_CELSIUS), va='top',
                transform=ax.transAxes, fontsize=textsize)
        ax.text(0.6, 0.1, 'min = %s %sC' % (minTemp, TEXT_CELSIUS),
                va='bottom', transform=ax.transAxes, fontsize=textsize)

        ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
        ax.grid(True)
        fig.autofmt_xdate()
        return fig

#    @deprecated
    def plotToFile(self, data, filename, title, xSize, ySize):
        """
        This function plots data and saves it to file.

        data -- tuple of (datetime, degree celsius float)-tuples
        filename -- full path of file string
        title -- string which is used as title of plot
        xSize -- width of the plot
        ySize -- height of the plot

        """
        # TODO: Error handling if no data is given
        if data is None or data == ():
            return False

        self.__plot__(data, title, xSize, ySize)

        self.fig.savefig(filename)
        return filename


    def plot_temp_to_file(cls, data, filename, title, axisLabels, dimensions):
        # TODO: Error handling if no data is given, or other params are bad
        if data is None or data == ():
            return False

        fig = cls.__plot(data, title, axisLabels, dimensions)
        fig.savefig(filename)
        return True

