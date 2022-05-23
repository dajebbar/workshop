import pandas as pd
import numpy as np


df = pd.read_csv('../../datafiles/stock.csv')
# print(df.head())
df['New'] = df.Price * 2
# print(df.head())
df['New (Sum of X and Z)'] = df.New + df.Price
# print(df.head())

df.drop(columns=['New', 'New (Sum of X and Z)'], inplace=True)
print(df.head())
