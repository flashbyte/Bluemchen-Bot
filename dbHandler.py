import pymysql
from init import db


class dbHandler(object):

    def __init__(self):
        self.__setDB(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])

    def __setDB(self, host, user, passwd, db):
        self.dbConf = {'host': host, 'user': user, 'passwd': passwd, 'db': db}

    def __connect(self):
        return pymysql.connect(
            host=self.dbConf['host'],
            user=self.dbConf['user'],
            passwd=self.dbConf['passwd'],
            db=self.dbConf['db']
        )

    def __execute(self, query):
        database = self.__connect()
        cursor = database.cursor()
        try:
            cursor.execute(query)
            database.commit()
        except:
            print('DB error')
            return None
        database.close()
        return cursor

    def __select(self, query):
        cursor = self.__execute(query)
        # return list(cursor.fetchall())
        return cursor.fetchall()

    def __insert(self, query):
        self.__execute(query)

    def getData(self, houres):
        """ Get data from database

        Keyword arguments:
        houres -- how many houres
        returns list of hashes
        """
        if houres <= 0:
            return None
        else:
            return self.__select('select * from temperatur_sensor where DATE_SUB(NOW(),INTERVAL %s HOUR) <= time and temperatur order by time asc;' % houres)

    # Write an filename in DB table http_requests row path
    def writeRequest(self, filename):
        self.__insert("""INSERT INTO plot_timestamps (path, time)
                           VALUES ('%s', CURRENT_TIMESTAMP())
                           ON DUPLICATE KEY UPDATE time = CURRENT_TIMESTAMP();""" % filename)

    # Checks DB for new Data
    def hasNewData(self, filename):
        dataTimestamps = self.__select('SELECT time FROM temperatur_sensor ORDER BY time DESC LIMIT 1;')
        plotTimestamps = self.__select("SELECT time FROM plot_timestamps WHERE path = '%s';" % filename)

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
