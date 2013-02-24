# Author: Nils Mull (mail@flash-byte.de)
# Date: 10.02.2013
import matplotlib
matplotlib.use('Agg')

import tempfile
#import time
import matplotlib.pyplot as plt
import pymysql
from init import db  # , dropbox


class tempPlot(object):
    """docstring for tempSensot
    Class for getting tempertur data from database, creating a plot and upload it to the blog.
    """
    def __init__(self):
        pass

    def __getData__(self, houres):
        """ Get data from database

        Keyword arguments:
        houres -- how many houres
        returns list of hashes
        """
        database = pymysql.connect(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])
        cursor = database.cursor()
        try:
            cursor.execute('select * from temperatur_sensor where DATE_SUB(NOW(),INTERVAL %s HOUR) <= time and temperatur order by time asc' % houres)
            database.commit()
        except:
            print('DB error')
            return None
        database.close()
        return list(cursor.fetchall())

    # TODO: X and Y Size
    def __plot__(self, houres, title):
        data = self.__getData__(houres)
        x = []
        y = []
        for i in data:
            x.append(i[0])
            y.append(i[1])
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Temperatur in C')
        ax.set_title(title)
        # TODO: Bad date fomate
        ax.plot(x, y)

    def plotToFile(self, houres, title):
        self.__plot__(houres, title)
        filename = tempfile.mkstemp(suffix='.png')[1]  # Don't need this!
        self.fig.savefig(filename)
        return filename