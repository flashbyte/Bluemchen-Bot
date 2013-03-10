# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, MinuteLocator, \
    WeekdayLocator, MonthLocator, DateFormatter, date2num

# constant for unicode degree symbol
TEXT_CELSIUS = u'\u00b0'


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
        elif period < timedelta(weeks=2):
            return cls.__day_locators(period)
        else:
            return cls.__month_locators(period)

    def __month_locators(cls, period):
        if period < timedelta(weeks=12):
            majorLocator = WeekdayLocator(byweekday=Mo, interval=1)
            majorFmt = DateFormater('%d.%m')
            minorLocator = DayLocator(interval=1)
            minorFmt = DateFormater('%d')
        else:
            majorLocator = Monthlocator(interval=1)
            majorFmt = DateFormater('%m.%Y')
            minorLocator = WeekdayLocator(byweekday=Mo, interval=1)
            minorFmt = DateFormater('%d')
        return majorLocator, majorFmt, minorLocator, minorFmt

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

        self.fig = plt.figure(figsize=pixelToInch(xSize, ySize, 100))
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in %sC' % (TEXT_CELSIUS))
        ax.set_title(title)
        ax.plot(x, y)

        majorLocator, majorFmt, minorLocator, minorFormat = \
            self.__get_locators(period)

        ax.plot_date(date2num(data[0][0]), data[0][1], '-')
        ax.xaxis.set_major_locator(majorLocator)
        ax.xaxis.set_major_formatter(majorFmt)
        ax.xaxis.set_minor_locator(minorLocator)
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
        self.fig.autofmt_xdate()

    def plotToFile(self, data, filename, title, xSize, ySize):
        # TODO: Error handling if no data is given
        if data is None or data == ():
            return False

        self.__plot__(data, title, xSize, ySize)

        self.fig.savefig(filename)
        return filename
