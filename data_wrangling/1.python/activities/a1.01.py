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
    dif = []
    l = 100
    for i in range(10):
        l1 = set_random_list(l)
        l2 = by_three(l1)
        dif.append(abs(len(l1) - len(l2)))
    l12 = list(set(l1))
    
    print(l12)
    print(dif)
    print(f'the mean is {find_mean(dif)}')

