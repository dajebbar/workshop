from sys import getsizeof

big_lst = [1 for _ in range(1, int(1e7))]
# print(big_lst)

size_big_lst = getsizeof(big_lst)
print(size_big_lst)