#!/usr/bin/python
# Script that takes a log file as an argument and produces a histogram
# args: logfile divisor(int) default is 3
#
# notes on divisor
# the divisor is used to prettify the histogram in order to make it fit on the page,
# for example 8000 divided by the default of three  is not going to fit on one line,
# so maybe the divisor should be 1000 or so
import sys
from os.path import isfile

# defaults
divisor = 3
botdic = {}
wordlist = ["bot", "Bot", "BOT", "crawler", "Crawler", "CRAWLER", "spider", "Spider", "SPIDER"]

# functions and subroutines
def wordsinstring(word_list, a_string):
    return set(word_list).intersection(a_string.split())

def usage():
	print """

USAGE: python botulizer.py <logfile> <int>

Scans specified log files for bots, crawlers, and spiders and prints a histogram

bar             | =========================== [27]
foo             | =============== [15]

"""


def graphify(botdic):
	for k in sorted(botdic, key=botdic.get, reverse=True):
		print "%-15s %s %s [%s]" % (k, "|", "=" * (botdic[k] / divisor), botdic[k])


# fail safe function check variables for legitimacy
def isSafe(f, i):
	errorCount = 0
	if not isfile(f):
		errorCount += 1
	if not isinstance(i, int):
		errorCount += 1
	if errorCount > 0:
		return False
	else:
		return True

# main function where all the partying happens
def startscan(logfile, divisor, wordlist):
	print "Scan started on file :", logfile
	print "Please wait...."
	with open(logfile) as f:
		for line in f:
			line = line.strip()
			for word in line.split():
				for pattern in wordlist:
					if pattern in word:
						botdic.setdefault(word, 0)
						botdic[word] = botdic[word] + 1 
	graphify(botdic)

# get number of arguments and go something depending on how many we get
if len(sys.argv) >3:
	usage()
	exit
elif len(sys.argv) == 1:
	usage()
	exit
elif len(sys.argv) == 3:
	logfile = sys.argv[1]
	divisor = int(sys.argv[2])
	# fail safe
	if isSafe(logfile, divisor):
		startscan(logfile, divisor, wordlist)
	else:
		print "Something went wrong, either the file doesnt exist or the divisor wasnt a valid integer.\n"
elif len(sys.argv) == 2:
	logfile = sys.argv[1]
	# fail safe
	if isSafe(logfile, divisor):
		startscan(logfile, divisor, wordlist)
	else:
		print "Something went wrong, either the file doesnt exist or the divisor wasnt a valid integer.\n"
