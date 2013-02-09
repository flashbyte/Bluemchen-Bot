#! /usr/bin/env python
import MySQLdb
import re
import sys

#2013/02/09 19:49:21 Temperature 76.78F 24.88C
def getTemp(text):
	result = re.search('\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.*?\d{2}.\d{2}F (\d{2}.\d{2})C',text)
	if result!='':
		tempString = result.group(0)
		return double(tempString)
	else:
		return None

print getTemp(sys.argv[1])

