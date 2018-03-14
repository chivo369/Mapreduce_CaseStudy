#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        temp = line[0]

        a= temp.split('#')
        print ('Severity %s: Priority %s:\t%s' % (a[4],a[3],1))

