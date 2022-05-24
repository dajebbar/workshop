import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


people = [
    'Ann','Brandon','Chen',
    'David','Emily','Farook',
    'Gagan','Hamish','Imran',
    'Joseph','Katherine','Lily'
]

age = [21,12,32,45,37,18,28,52,5,40,48,15]
weight = [55,35,77,68,70,60,72,69,18,65,82,48]
height = [160,135,170,165,173,168,175,159,105,171,155,158]

people_dict={
    'People':people,
    'Age':age,
    'Weight':weight,
    'Height':height
}

people_df=pd.DataFrame(data=people_dict)
# print(people_df)

print(people_df.shape)
print(people_df.Age.count())

print(people_df.Age.sum())
print(people_df.Age.mean())
print(people_df.Weight.median())
print(f'min max height: {people_df.Height.min()}, {people_df.Height.max()}')

pcnt_75 = np.percentile(people_df.Weight, 75)
pcnt_25 = np.percentile(people_df.Weight, 25)
iqr = pcnt_75 - pcnt_25

print(f'Inter-quartile range: {iqr}')
