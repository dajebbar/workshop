import random
from random import seed
import math

seed(42)

def set_random_list(l):
    return [random.randint(0, 50) for _ in range(l)]

def by_three(l):
    return [x for x in l if x % 3 ==0]

def find_mean(lst):
    pass