import pandas as pd
from datetime import datetime

a = pd.Timestamp('2012-01-15')
print("a)", a)

b = pd.Timestamp('2024-01-01 21:20:00')
print("b)", b)

c = pd.Timestamp.now()
print("c)", c)

d = pd.to_datetime('2024-01-01').date()
print("d)", d)

e = pd.Timestamp.today().date()
print("e)", e)

f = pd.Timestamp.now().time()
print("f)", f)

g = datetime.now().time()
print("g)", g)
