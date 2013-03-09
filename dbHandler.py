import pymysql
from init import db


class dbHandler(object):

    def __init__(self):
        self.__setDB__(host=db['host'], user=db['user'], passwd=db['passwd'], db=db['db'])

    def __setDB__(self, host, user, passwd, db):
        self.dbConf = {'host': host, 'user': user, 'passwd': passwd, 'db': db}

    def getData(self, houres):
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

    # Write an filename in DB table http_requests row path
    def writeRequest(self, filename):
        pass

    # Checks DB for new Data
    def hasNewData(self):
        pass
