#! /usr/bin/env python
# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
#import twitter
#import cal
#import time
#import init
#import tempPlot
import optparse


parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
