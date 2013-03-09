#! /usr/bin/env python
# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
#import twitter
#import cal
#import time
#import init
import tempPlot
import dbHandler

db = dbHandler.dbHandler()
data = db.getData(houres=24)
db.writeRequest('Aasdfadsfsadf')
print(db.hasNewData('Aasdfadsfsadf'))


tp = tempPlot.tempPlot()
print (tp.plotToFile(data, 'Test Plot', 400, 300))
