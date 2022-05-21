import random
from random import seed

seed(42)

lst_1 = [random.randint(0, 30) for _ in range(101)]
print(lst_1)

# find the square of each element
lst_2 = [x**2 for x in lst_1]
print(lst_2)