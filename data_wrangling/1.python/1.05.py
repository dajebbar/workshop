import random
from random import seed
import math

seed(42)

lst_1 = [random.randint(0, 30) for _ in range(101)]
print(lst_1)

# find the square of each element
lst_2 = [x**2 for x in lst_1]
print(lst_2)

# find the log
lst_3 = [round(math.log10(x), 3) for x in lst_1 if x > 0]
print(lst_3[:3])