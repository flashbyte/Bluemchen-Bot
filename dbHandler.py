import pymysql
from init import db


class dbHandler(object):

    def __init__(self):
        self.__setDB__(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])

    def __setDB__(self, host, user, passwd, db):
        self.dbConf = {'host': host, 'user': user, 'passwd': passwd, 'db': db}

    def __connect__(self):
        return pymysql.connect(
            host=self.dbConf['host'],
            user=self.dbConf['user'],
            passwd=self.dbConf['passwd'],
            db=self.dbConf['db']
        )

    def __execute__(self, query):
        database = self.__connect__()
        cursor = database.cursor()
        try:
            cursor.execute(query)
            database.commit()
        except:
            print('DB error')
            return None
        database.close()
        return cursor

    def __select__(self, query):
        cursor = self.__execute__(query)
        # return list(cursor.fetchall())
        return cursor.fetchall()

    def __insert__(self, query):
        self.__execute__(query)

    def getData(self, houres):
        """ Get data from database

        Keyword arguments:
        houres -- how many houres
        returns list of hashes
        """
        if houres <= 0:
            return None
        else:
            return self.__select__('select * from temperatur_sensor where DATE_SUB(NOW(),INTERVAL %s HOUR) <= time and temperatur order by time asc;' % houres)

    # Write an filename in DB table http_requests row path
    def writeRequest(self, filename):
        self.__insert__("""INSERT INTO plot_timestamps (path, time)
                           VALUES ('%s', CURRENT_TIMESTAMP())
                           ON DUPLICATE KEY UPDATE time = CURRENT_TIMESTAMP();""" % filename)

    # Checks DB for new Data
    def hasNewData(self, filename):
        dataTimestamps = self.__select__('SELECT time FROM temperatur_sensor ORDER BY time DESC LIMIT 1;')
        plotTimestamps = self.__select__("SELECT time FROM plot_timestamps WHERE path = '%s';" % filename)

        if (len(dataTimestamps) == 0):
            retval = False
        else:
            if (len(plotTimestamps) == 0):
                retval = True
            else:
                lastDataTimestamp = dataTimestamps[0][0]
                lastPlotTimestamp = plotTimestamps[0][0]

                retval = (lastPlotTimestamp < lastDataTimestamp)

        return retval
