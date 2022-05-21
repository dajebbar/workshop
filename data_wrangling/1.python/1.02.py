import pandas as pd


ssn = list(pd.read_csv('./datasets/ssn.csv'))

# append to a new list
ssn2 = []
for item in ssn:
    ssn2.append(item)

print(ssn2)

# generate a list with a comprehension list
ssn3 = [f'soc:{item}' for item in ssn2]
print(ssn3)

# iterate list with while loop
i = 0
while i < len(ssn3):
    print(ssn3[i])
    i += 1
