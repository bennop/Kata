#!/usr/bin/env python
import pandas as pd
index = 2

f=open(__file__, "r")
fl = f.readlines()
f.close()
mylines = len(fl)

infile = 'file%d.csv' % index
old = pd.read_csv(infile, header = None)
#print(old.iloc[1,1])
old.append = ("Sylvain",
            mylines, old.iloc[index-1,2]+mylines)

old.to_csv('file3.csv', header = False,index = False)

f = open("file3.csv","a+")     # "a" for append
# since to_csv does not add spaces after comma, adjust output format here
f.write("'Sylvain',%d,%d\n" % (mylines, old.iloc[1,2]+mylines))
f.close()
