# botulizer

Scans specified log files for bots, crawlers, and spiders and prints a histogram
bar             | =========================== [27]
foo             | =============== [15]


# Script that takes a log file as an argument and produces a histogram
# args: logfile divisor(int) default is 3
#
# notes on divisor
# the divisor is used to prettify the histogram in order to make it fit on the page,
# for example 8000 divided by the default of three  is not going to fit on one line,
# so maybe the divisor should be 1000 or so
