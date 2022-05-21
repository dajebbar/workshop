import random
from random import seed
import math

seed(42)

def set_random_list(l):
    return [random.randint(0, 50) for _ in range(l)]

def find_mean(lst):
    pass