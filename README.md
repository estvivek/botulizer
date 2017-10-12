# botulizer

```
Scans specified log files for bots, crawlers, and spiders and prints a histogram
bar             | =========================== [27]
foo             | =============== [15]
```

Script that takes STDIN as data and an optional divisor as an argument and produces a histogram
args: logfile divisor(int) default is 3

notes on divisor

the divisor is used to prettify the histogram in order to make it fit on the page,
for example 8000 divided by the default of three  is not going to fit on one line,
so maybe the divisor should be 1000 or so but feel free to play with integers until
it looks nice / fits on whatever mediia you want to paste the report.


# examples

default divisor (3)

```
$ cat logfile | ./botulizer.py
Scan started, please wait....
YandexBot/3.0;                 | ======== [26]
Googlebot/2.1;                 | == [8]
Baiduspider/2.0;               | == [6]
AhrefsBot/5.2;                 | = [5]
bingbot/2.0;                   | = [3]
(Applebot/0.1;                 |  [2]
```

compressed file (use zcat with a pipe):

```
$ gzip logfile
$ zcat logfile.gz | ./botulizer.py
Scan started, please wait....
YandexBot/3.0;                 | ======== [26]
Googlebot/2.1;                 | == [8]
Baiduspider/2.0;               | == [6]
AhrefsBot/5.2;                 | = [5]
bingbot/2.0;                   | = [3]
(Applebot/0.1;                 |  [2]
```
