#! /usr/bin/env python
import MySQLdb
import re
import sys


def getTemp(text):
	result = re.search('\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.*?\d{2}.\d{2}F (\d{2}.\d{2})C',text)
	if result:
		tempString = result.group(0)
		return double(tempString)
	else:
		return None

print getTemp(sys.argv[1])

