#! /usr/bin/env python
import re
import sys
import pymysql


#2013/02/09 19:49:21 Temperature 76.78F 24.88C
def getTemp(text):
    result = re.search('\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.*?\d{2}.\d{2}F (\d{2}.\d{2})C', text)
    if result != None:
        tempString = result.groups()[0]
        return float(tempString)
    else:
        print('Parsing Error')
        return None


def postTempToDB(temperatur):

    db = pymysql.connect(host='poseidon', user='wg_bot', passwd='umpalumpa', db='wg_database')
    cursor = db.cursor()

    if temperatur:

        sql = """INSERT INTO temperatur_sensor(temperatur)
                 VALUES ('%f')""" % temperatur
    else:
        sql = """INSERT INTO temperatur_sensor(temperatur)
                 VALUES (NULL)"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    db.close()

# postTempToDB(getTemp(sys.argv[1]))
inputText = sys.stdin.readline()

if inputText != None:
    postTempToDB(getTemp(inputText))
else:
    postTempToDB(getTemp(sys.argv[1]))
