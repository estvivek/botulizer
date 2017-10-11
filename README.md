# botulizer

```
Scans specified log files for bots, crawlers, and spiders and prints a histogram
bar             | =========================== [27]
foo             | =============== [15]
```

Script that takes a log file as an argument and produces a histogram
args: logfile divisor(int) default is 3

notes on divisor

the divisor is used to prettify the histogram in order to make it fit on the page,
for example 8000 divided by the default of three  is not going to fit on one line,
so maybe the divisor should be 1000 or so


# examples

default divisor (3)

```
$ python botulizer.py logfile
Scan started on file : logfile
Please wait....
mj12bot         | ================ [50]
baiduspider     | ======= [23]
yandexbot       | ===== [17]
Ahrefsbot       | == [6]
PinterestBot    | = [5]
Semrshbot       | = [3]
$
```

with setting divisor to 10

```
$ python botulizer.py logfile 10
Scan started on file : logfile
Please wait....
mj12bot         | ===== [50]
baiduspider     | == [23]
yandexbot       | = [17]
Ahrefsbot       |  [6]
PinterestBot    |  [5]
Semrshbot       |  [3]
$
```
