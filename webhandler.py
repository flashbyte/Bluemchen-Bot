
import tempSens

def getGraph(req,houres=24,title='Temperatur',xSize=800,ySize=600):
    text = "You will get an Graph with size %sx%s and the Title:%s which will show the last %s houres" %(xSize,ySize,title,houres)
    g = tempSens.tempSensor()
    g.plotToFile(houres,'/tmp/test.png','WebTest')
    req.sendfile('/tmp/test.png')


