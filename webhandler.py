#from mod_python import apache
import tempPlot
import dbHandler
import os


# http://localhost/Bluemchen-Bot/webhandler.py/getGraph?houres=24&xSize=400&ySize=300&title=Hallo
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
    if db.hasNewData(filename):
        data = db.getData(houres)
        g.plotToFile(data, filename, title, xSize, ySize)

    # Check if file exits:
    if not os.path.exists(filename):
        return "ERROR"

    req.content_type = 'image/png'
    req.sendfile(filename)


def getLastDay(req, title='Temperatur 24h', xSize=800, ySize=600):
    __getPlot__(req, 'day', 'dayPlot.png', title, xSize, ySize)


def getLastWeek(req, title='Temperatur 7d', xSize=800, ySize=600):
    __getPlot__(req, 'week', 'weekPlot.png', title, xSize, ySize)


def getLastMonth(req, title='Temperatur 1 Month ', xSize=800, ySize=600):
    __getPlot__(req, 'month', 'monthPlot.png', title, xSize, ySize)


def getLastYear(req, title='Temperatur 1 Year', xSize=800, ySize=600):
    __getPlot__(req, 'year', 'yearPlot.png', title, xSize, ySize)
