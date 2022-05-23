import numpy as np

lst1 = [1,2,3]
arr1 = np.array(lst1)
# print(arr1)

a = np.array([1.2, 3.4, 5.6])
# print(a, type(a))

data = np.genfromtxt('../../datafiles/stock.csv', delimiter=',', names=True, dtype=None, encoding='ascii')
print(data)