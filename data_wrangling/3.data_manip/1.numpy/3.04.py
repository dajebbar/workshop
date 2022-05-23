import pandas as pd
import numpy as np

df = pd.read_csv('../../datafiles/numbers.csv', names=['nums'])
# print(df.head())

lst5 = df.to_numpy().tolist()
# print(lst5[:5])

arr5 = np.array(lst5)
print(arr5[:5])