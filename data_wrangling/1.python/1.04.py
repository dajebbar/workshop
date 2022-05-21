import pandas as pd


ssn = list(pd.read_csv('./datasets/ssn.csv'))

list_1 = [*range(1,21)]

# sort list with reverse=True
list_2 = sorted(list_1, reverse=True)
print(list_2)


print(list(reversed(list_2)))

