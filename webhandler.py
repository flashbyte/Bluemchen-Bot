# Author Nils Mull (mail@flash-byte.de)
# Date 2013-03-09
import tempPlot
import dbHandler
import os
from mod_python import apache
# Class for Handling webrequest via mod_python
# Example: http://localhost/Bluemchen-Bot/
# webhandler.py/getLastDay?xSize=400&ySize=300&title=Hallo


def __getPlot__(req, plot, filename, title, xSize, ySize):
    db = dbHandler.dbHandler()
    g = tempPlot.tempPlot()
    if plot == 'day':
        houres = 24
    if plot == 'week':
        houres = 24 * 7
    if plot == 'month':
        houres = 24 * 7 * 30
    if plot == 'year':
        houres = 24 * 365

    # Check for new Data
    if db.hasNewData('/tmp/' + filename):
        data = db.getData(houres)
        g.plotToFile(data, '/tmp/' + filename, title, int(xSize), int(ySize))
        db.writeRequest('/tmp/' + filename)

    # Check if file exits:
    if not os.path.exists('/tmp/' + filename):
        return apache.HTTP_NOT_FOUND

    req.content_type = 'image/png'
    req.sendfile('/tmp/' + filename)


# Webrequest for 23 hour plot
def getLastDay(req, title='Temperatur 24h', xSize=800, ySize=600):
    __getPlot__(req, 'day', 'dayPlot.png', title, xSize, ySize)


# Webrequest for 7 day plot
def getLastWeek(req, title='Temperatur 7d', xSize=800, ySize=600):
    __getPlot__(req, 'week', 'weekPlot.png', title, xSize, ySize)


# Webrequest for 1 month plot
def getLastMonth(req, title='Temperatur 1 Month ', xSize=800, ySize=600):
    __getPlot__(req, 'month', 'monthPlot.png', title, xSize, ySize)


# Webrequest for one year plot
def getLastYear(req, title='Temperatur 1 Year', xSize=800, ySize=600):
    __getPlot__(req, 'year', 'yearPlot.png', title, xSize, ySize)
