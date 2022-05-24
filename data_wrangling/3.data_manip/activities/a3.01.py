import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
plt.style.use('ggplot')

url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Wrangling-Workshop/master/Chapter03/datasets/Boston_housing.csv'
urlretrieve(url, 'boston.csv')

df = pd.read_csv('boston.csv')
print(df.head())