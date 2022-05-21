import pandas as pd


ssn = list(pd.read_csv('./datasets/ssn.csv'))

# append to a new list
ssn2 = []
for item in ssn:
    ssn2.append(item)

print(ssn2)