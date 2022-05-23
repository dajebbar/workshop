import pandas as pd
import numpy as np

df = pd.read_csv('../../datafiles/numbers.csv', names=['nums'])
print(df.head())
print('\n*** * 9\n')
lst5 = df.to_numpy().tolist()
print(lst5[:5])
print('\n*** * 9\n')
arr5 = np.array(lst5)
print(arr5[:5])
print('\n*** * 9\n')

# find the sine of arr5

print(np.sin(arr5[:5]))
print(np.log(arr5[:5]))