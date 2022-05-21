import pandas as pd


ssn = list(pd.read_csv('./datasets/ssn.csv'))
print(ssn)
print(ssn[0])
print(ssn[3])
print(ssn[-1])
print(f'Length of ssn list: {len(ssn)}')
print(ssn[1:3])
# reverse elements
print(ssn[-1::-1])