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
		print "%-30s %s %s [%s]" % (k, "|", "=" * (botdic[k] / divisor), botdic[k])

def sanitize(botdic):
	banlist = ["robots.txt", "Robots.txt", "ROBOTS.TXT",
		"bottom", "Bottom", "BOTTOM",
		"botany", "Botany", "BOTANY",
		"both", "Both, BOTH",
		"https", "http"]
	for k in botdic.keys():
		for pattern in banlist:
			if pattern in k:
				# failsafe, first check if key exists, then delete
				if k in botdic:
					del botdic[k]	 

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
	sanitize(botdic)
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
	if divisor == "0":
		print "Something went wrong, the divisor specified wasnt a valid integer."
		print "The divisor specified cannot be zero.\n"
		sys.exit()
		
	try:
		divisor = int(sys.argv[1])
	except:
		print "Something went wrong, the divisor specified wasnt a valid integer."
		print "Divisor:", divisor, "\n"
		sys.exit()
	startscan(divisor, wordlist)
