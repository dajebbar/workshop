import numpy as np


list_1 = [1,2,3]
array_1 = np.array(list_1)

list_2 = list_1 + list_1
print(list_2)

array_2 = array_1 + array_1
print(array_2)

data = np.genfromtxt('../../datafiles/numbers.csv', delimiter=',', names=['nums'])
data = data.astype('float64')
print(data+data)