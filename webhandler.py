#from mod_python import apache
import tempPlot


# http://localhost/Bluemchen-Bot/webhandler.py/getGraph?houres=24&xSize=400&ySize=300&title=Hallo
def getGraph(req, houres=24, title='Temperatur', xSize=800, ySize=600):
    #text = "You will get an Graph with size %sx%s and the Title:%s which will show the last %s houres" % (xSize, ySize, title, houres)
    g = tempPlot.tempPlot()
    filename = g.plotToFile(houres, title, int(xSize), int(ySize))
    req.content_type = 'image/png'
    req.sendfile(filename)
