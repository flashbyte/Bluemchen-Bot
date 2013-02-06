#! /usr/bin/env python
# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
import twitter
import cal
import time

scedule=[
('Monday 9:00',putzplan())
]

# Start Deamon
while True:
	# ----- Do Stuf -----
	print "RUN:%s" %(time.asctime())
	wd=time.strftime('%w')

	# -------------------
	time.sleep(60*5)