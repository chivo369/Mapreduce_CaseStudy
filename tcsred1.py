#!/usr/bin/env python

from operator import itemgetter
import sys

pre = None
val = 0
word = None

for line in sys.stdin:
    # remove  whitespace
    line = line.strip()
    # split the input from the \t
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if pre == word:
        val += count
    else:
        if pre:
            print ('%s\t Count of incidents:%s' % (pre, val))
        val = count
        pre = word

if pre == word:
    print ('%s\t Count of incidents:%s' % (pre, val))

