import pandas as pd
import numpy as np


df = pd.read_csv("../../datafiles/numbers2.csv", header=None)
list2d = df.values
mat1 = np.array(list2d)

print(mat1.shape)
print(f'dimension: {mat1.ndim}')
print(f'size: {mat1.size}')
print(f'data type of the Matrix: {mat1.dtype}')