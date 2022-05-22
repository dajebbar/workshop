from sys import getsizeof
from itertools import repeat

big_lst = [1 for _ in range(1, int(1e7))]
# print(big_lst)

size_big_lst = getsizeof(big_lst)
print(size_big_lst)

# get less memory

small_lst = repeat(1, times=int(1e7))
size_small_lst = getsizeof(small_lst)
print(size_small_lst)

for index, item in enumerate(small_lst, 1):
    print(item, end=' ')
    if index > 20:
        break
