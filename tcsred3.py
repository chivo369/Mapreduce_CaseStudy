#!/usr/bin/env python

from operator import itemgetter
import sys

a=b=c=d=e=0
f=[]
g=[]
h=[]
i=[]
j=[]

for line in sys.stdin:
    # remove  whitespace
    line = line.strip()
    # split the input from the \t
    word = line.split('\t')
    if word[0]=='1-Critical':
        if int(word[1])>=a:
            if int(word[1])==a:
                a=int(word[1])
                f.append(word[2])
            elif int(word[1])>a:
                del f[:]
                a=int(word[1])
                f.insert(0, word[2])
                
    elif word[0]=='2-High':
        if int(word[1])>=b:
            if int(word[1])==b:
                b=int(word[1])
                g.append(word[2])
            elif int(word[1])>b:
                del g[:]
                b=int(word[1])
                g.insert(0, word[2]) 

    elif word[0]=='3-Medium':
        if int(word[1])>=c:
            if int(word[1])==c:
                c=int(word[1])
                h.append(word[2])
            elif int(word[1])>c:
                del h[:]
                c=int(word[1])
                h.insert(0, word[2]) 

    elif word[0]=='4-Low':
        if int(word[1])>=d:
            if int(word[1])==d:
                d=int(word[1])
                i.append(word[2])
            elif int(word[1])>d:
                del i[:]
                d=int(word[1])
                i.insert(0, word[2]) 

    elif word[0]=='5-When Possible':
        if int(word[1])>=e:
            if int(word[1])==e:
                e=int(word[1])
                j.append(word[2])
            elif int(word[1])>e:
                del j[:]
                e=int(word[1])
                j.insert(0, word[2]) 
                


print('Urgency Critical : Incident no: %s') % ((f))
print('Urgency High : Incident no: %s') % ((g))
print ('Urgency Medium : Incident no: %s') % ((h))
print('Urgency Low : Incident no: %s') % ((i))
print ('Urgency When Possible : Incident no: %s') % ((j))

