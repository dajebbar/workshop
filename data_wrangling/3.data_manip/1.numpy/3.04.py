import pandas as pd


df = pd.read_csv('../../datafiles/numbers.csv', names=['nums'])
# print(df.head())

lst5 = df.to_numpy().tolist()
print(lst5[:5])