import re
import time
import pylab
fh = open('temperatur.txt')

lines=fh.readlines()

#2013/01/24 20:31:37 Temperature 75.42F 24.12C\n'

data=[]
for line in lines:
	result = re.search('(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}).*?\d{2}.\d{2}F (\d{2}.\d{2})C',line)
	if result != None:
		timeString = result.group(1)
		temperatur = result.group(2)
		#tmp = {'time':time.strptime(timeString,'%Y/%m/%d %H:%M:%S'),'temperatur':float(temperatur)}
		data.append(temperatur)


pylab.plot(data)
pylab.show()

fh.close()