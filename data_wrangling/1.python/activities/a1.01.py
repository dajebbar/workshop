import random
# from random import seed

# seed(42)

def set_random_list(l):
    return [random.randint(0, 50) for _ in range(l)]

def by_three(l):
    return [x for x in l if x % 3 ==0]

def find_mean(lst):
    return sum(lst)/len(lst)

if __name__=='__main__':
    l = 100
    l1 = set_random_list(l)
    l2 = by_three(l1)
    dif = abs(len(l1) - len(l2))