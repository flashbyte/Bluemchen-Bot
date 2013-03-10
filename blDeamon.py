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
#data = db.hasNewData('tets')

#print data
# db.writeRequest('Aasdfadsfsadf')
# print(db.hasNewData('Aasdfadsfsadf'))

data = db.getData(2400)

tp = tempPlot.tempPlot()
print (tp.plotToFile(data, 'test.png', 'Test Plot', 400, 300))
