#!/usr/bin/env python
import pandas as pd

f = open(__file__, "r")
fl = f.readlines()
f.close()
mylines = len(fl)

old = pd.read_csv('file2.csv', header = None)
new = pd.Series(["'Sylvain'", mylines, old.iloc[1, 2] + mylines])
new_df = old.append(new, ignore_index = True)

# writes output without spaces
new_df.to_csv('file3b.csv', header = False, index = False)
