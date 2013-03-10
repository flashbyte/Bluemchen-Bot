# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
from init import calenderConfig
#import time
import requests
import xml.etree.ElementTree as ElementTree


class Cal(object):
    def __init__(self):
        self.icalUrl = calenderConfig['icalUrl']
        self.__getCal__()
        self.__parseCal__()

    def __getCal(self):
        try:
            self.__req__ = requests.get(self.icalUrl)
        except:
            print ("Could not fetch Calender")

    def __parseCal(self):
        prefix = '{http://www.w3.org/2005/Atom}'
        text = self.__req__.content
        rootElement = ElementTree.fromstring(text.encode('ascii', 'ignore'))
        entries = rootElement.findall(prefix + 'entry')
        for entry in entries:
            print entry.find(prefix + 'title').text
