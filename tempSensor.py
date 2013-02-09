#! /usr/bin/env python
import pymysql


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

postTempToDB(None)
