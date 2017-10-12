#!/usr/bin/python
# Script that takes logdata from stdin an argument and produces a histogram
# args: divisor(int) default is 3
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
def startscan(divisor, wordlist):
	print "Scan started, please wait...."
	for line in sys.stdin:
		line = line.strip()
		for word in line.split():
			for pattern in wordlist:
				if pattern in word:
					botdic.setdefault(word, 0)
					botdic[word] = botdic[word] + 1
	graphify(botdic)

# get number of arguments and go something depending on how many we get
if len(sys.argv) == 1:
	startscan(divisor, wordlist)
elif len(sys.argv) > 2:
	usage()
	sys.exit()
else:
	divisor  = sys.argv[1]
	# fail safe
	try:
		divisor = int(sys.argv[1])
	except:
		print "Something went wrong, the divisor specified wasnt a valid integer.\n"
		print "Divisor:", divisor
		sys.exit()
	startscan(divisor, wordlist)
