import pandas as pd


df = pd.read_csv('../../datafiles/numbers.csv', names=['nums'])
print(df.head())