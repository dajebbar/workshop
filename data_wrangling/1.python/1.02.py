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

# Search all the social security numbers with the number 5 in them
ssn_with5 = [item for item in ssn3 if '5' in item]
print(f'social security containing # 5:\n{ssn_with5}')

# Generate a list by adding the two lists
ssn_4 = ["102-90-0314" , "247-17-2338" , "318-22-2760"]
ssn_5 = ssn_4 + ssn
print(ssn_5)

# Extend a string using the extend keyword
ssn2.extend(ssn_4)
print(ssn2)

# loop over the first list and create a nested list inside that loop that
# goes over the second list
for x in ssn2:
    for y in ssn_5:
        print(f'{x} , {y}')