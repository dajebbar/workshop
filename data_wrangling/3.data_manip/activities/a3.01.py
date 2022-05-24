import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
plt.style.use('ggplot')

url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Wrangling-Workshop/master/Chapter03/datasets/Boston_housing.csv'
urlretrieve(url, 'boston.csv')

df = pd.read_csv('boston.csv')
# print(df.head())

# total number of records
# print(df.shape)

# smaller DataFrame with columns that do not include CHAS, NOX, B, and LSTAT

new_df = df.drop(columns=['CHAS', 'NOX', 'B', 'LSTAT'])
# print(new_df.head())

# nan values
# print(new_df.isna().sum())

# histogram
# plt.hist(new_df)
# print(plt.show())

# print(new_df.columns)
# plt.scatter(x=new_df.CRIM, y=new_df.PRICE)
# print(plt.show())

# plt.scatter(x=np.log(new_df.CRIM), y=new_df.PRICE)
# print(plt.show())

print(new_df.RM.mean())
print(new_df.AGE.median())
print(new_df.DIS.mean())
print((new_df.PRICE < 20).mean() * 100.)