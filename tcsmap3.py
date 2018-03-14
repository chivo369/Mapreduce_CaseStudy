#!/usr/bin/env python

from datetime import datetime
import time
import sys


fmt = '%m/%d/%Y %I:%M %p'
i=0

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")    
    temp = line[0]
    a= temp.split('#')
    y=str(a[10])
    x=" 12:00 AM"
    m=y+x
    t=a[11]
    index=t.find('13 ')
    out=t[:index] + '20' + t[index:]
    d1 = datetime.strptime(m, fmt)
    d2 = datetime.strptime(out, fmt)
    daysDiff = (d2-d1).seconds
    #print (daysDiff)
    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())
    diff=d2_ts-d1_ts
    # They are now in seconds, subtract and then divide by 60 to get minutes.
    #print (min_diff)

    print ('%s\t%d\t%s' % (a[6],diff,a[0]))


