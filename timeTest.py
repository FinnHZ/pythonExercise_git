import math
from datetime import datetime as dt


d = "2023-03-07"
dd = dt.strptime(d, "%Y-%m-%d")
print(dd, type(dd))

nowd = dt.now()
print(nowd, type(nowd))