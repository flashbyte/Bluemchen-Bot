#! /usr/bin/env python
import MySQLdb
import re
import subprocess


def getTemp():
	try:
		res = subprocess.check_output(["/usr/bin/pcsensor"])
		result = re.search('\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}.*?\d{2}.\d{2}F (\d{2}.\d{2})C',line)
		if result != None:
			tempString = result.group(0)
			return tempString
		else:
			print "Debug 1"
			return ''
	except:
		# print "Debug 2"
		return ''

print getTemp()

