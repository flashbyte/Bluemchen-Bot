import time
import pylab
import pymysql
from init import db

class tempSensor(object):
    """docstring for tempSensot
    Class for getting tempertur data from database, creating a plot and upload it to the blog.
    """
    def __init__(self):
        data = self.getData(24)
        self.plot(data)

    def getData(self,houres):
        """ Get data from database

        Keyword arguments:
        houres -- how many houres
        returns list of hashes
        """
        database = pymysql.connect(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])
        cursor = database.cursor()
        try:
            cursor.execute('select * from temperatur_sensor where DATE_SUB(NOW(),INTERVAL %s HOUR) <= time and temperatur order by time asc' %houres)
            database.commit()
        except:
            print('DB error')
            return None
        database.close()
        return list(cursor.fetchall())

    def plot(self,data):
        x=[]
        y=[]
        for i in data:
            x.append(i[0])
            y.append(i[1])
        pylab.plot(x,y)
        pylab.savefig('temperatur')