import pandas as pd

cm = list(pd.read_csv('./datasets/car_models.csv'))
print(cm)

# Check whether the strings D150 and Mustang are in the list
print('D150' in cm)
print('Mustang' in cm)

# pythonic way to iterating over loop
for item in cm:
    print(item)