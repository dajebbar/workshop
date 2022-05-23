import numpy as np


a = np.random.randint(0, 99, (30,))
b = a.reshape(2,3,5)
c = b.reshape(15, 2)

print(a)
print()
print(b)
print()
print(c)

b_flat = b.ravel()
print(b_flat)