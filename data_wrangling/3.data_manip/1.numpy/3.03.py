import numpy as np


data = np.genfromtxt('../../datafiles/numbers.csv', delimiter=',', names=['nums'])
data = data.astype('float64')

print(data * 45)
print(data / 67.7)

lst_1 = [1,2,3]
ar1 = np.array(lst_1)

print(f'array_1 raised to the power of array_1: {ar1**ar1}')