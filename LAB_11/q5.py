import numpy as np
a = np.array(input().split(), dtype=str)
print(np.char.center(a, 15, "_"))
print(np.char.rjust(a, 15, "_"))
print(np.char.ljust(a, 15, "_"))
