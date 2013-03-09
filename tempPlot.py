# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
import pymysql
from init import db  # , dropbox
from datetime import timedelta
from matplotlib.dates import DayLocator, HourLocator, DateFormatter
from matplotlib.finance import quotes_historical_yahoo

def pixelToInch(xSize, ySize, dpi):
    return (xSize / dpi, ySize / dpi)


class tempPlot(object):
    """docstring for tempSensot
    Class for getting tempertur data from database, creating a plot and upload it to the blog.
    """
    def __init__(self):
        self.__setDB__(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])
        pass

    def __setDB__(self, host, user, passwd, db):
        self.dbConf = {'host': host, 'user': user, 'passwd': passwd, 'db': db}

    def __getData__(self, houres):
        """ Get data from database

        Keyword arguments:
        houres -- how many houres
        returns list of hashes
        """
        if houres <= 0:
            return None
        database = pymysql.connect(
            host=self.dbConf['host'],
            user=self.dbConf['user'],
            passwd=self.dbConf['passwd'],
            db=self.dbConf['db']
            )
        cursor = database.cursor()
        try:
            cursor.execute('select * from temperatur_sensor where DATE_SUB(NOW(),INTERVAL %s HOUR) <= time and temperatur order by time asc' % houres)
            database.commit()
        except:
            print('DB error')
            return None
        database.close()
        return list(cursor.fetchall())

    def __plot__(self, houres, title, xSize=500, ySize=400):
        data = self.__getData__(houres)
        x = []
        y = []
        for i in data:
            x.append(i[0])
            y.append(i[1])

        first = data[0][0]
        last = i[0]
 
        days = DayLocator() # every day
        daysFmt = DateFormatter('%d')
        hours6 = HourLocator(interval=6) # every 6 hour
        hours = HourLocator() # every hour
        hoursFmt = DateFormatter('%H:%M')

        quotes = quotes_historical_yahoo('INTC', first, last)
        if len(quotes) == 0:
            print ('Found no quotes')
            raise SystemExit

        dates = [q[0] for q in quotes]
        opens = [q[1] for q in quotes]

        self.fig = plt.figure(figsize=pixelToInch(xSize, ySize, 100))
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in C')
        ax.set_title(title)
        # TODO: Bad date fomate
        ax.plot(x, y)

        ax.plot_date(dates, opens, '-')
        ax.xaxis.set_major_locator(hours6)
        ax.xaxis.set_major_formatter(hoursFmt)
        ax.xaxis.set_minor_locator(hours)

        ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
        ax.grid(True)
        self.fig.autofmt_xdate()

    def plotToFile(self, houres, title, xSize, ySize):
        self.__plot__(houres, title, xSize, ySize)
        filename = tempfile.mkstemp(suffix='.png')[1]  # Don't need this!
        self.fig.savefig(filename)
        return filename
