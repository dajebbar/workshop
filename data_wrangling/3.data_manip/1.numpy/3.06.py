import numpy as np
import pandas as pd


df = pd.read_csv('../../datafiles/numbers.csv', header=None)

list2d = df.values

mat1 = np.array(list2d)
print(f'Type/Class of this object: {type(mat1)}')
print(f'Here is the Matrix:\n{"---"* 6}\n{mat1}\n{"---"* 6}')