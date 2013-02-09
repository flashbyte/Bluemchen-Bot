#! /usr/bin/env python
import mport MySQLdb

db = MySQLdb.connect(host='poseidon',user='wg_bot',passwd='umpalumpa',db='wg_database')



db.close()