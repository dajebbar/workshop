import numpy as np
import pandas as pd


labels = ['a','b','c']
my_data = [10,20,30]
array_1 = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(data=array_1))
print(pd.Series(data=labels))

print(f'Holding functions:\n{"--"*8}\n{pd.Series(data=[sum, print, len])}')
print(f'Holding objects from a dictionary:\n{"--"*8}\n{pd.Series(data=[d.keys, d.values, d.items])}')

