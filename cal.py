# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
from init import calenderConfig
import urllib

class Cal(object):
	def __init__(self):
		self.icalUrl=calenderConfig['icalUrl']		
		self.__getCal__()
		self.__findEvents_()


	def __getCal__(self):
		ical = urllib.urlopen(self.icalUrl)
		lines = ical.readlines()
		self.calender=[]
		for line in lines:
			self.calender.append(line.rstrip())
		ical.close()

	def __findEvents_(self):
		inEvent=False
		self.events=[]
		for line in self.calender:
			if 'BEGIN:VEVENT' in line:
				inEvent=True
				event={}
			if inEvent == True:
				if 'DTSTART' in line:
					event['date']=(line.split(':')[1])
				if 'SUMMARY' in line:
					event['summary']=(line.split(':')[1])
				if 'RRULE' in line:
					event['interval']=((line.split(':')[1]).split(';')[1]).split('=')[1]
			if 'END:VEVENT' in line:
				inEvent=False
				self.events.append(event)
		print self.events	
