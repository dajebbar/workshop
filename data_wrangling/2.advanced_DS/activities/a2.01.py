import itertools

perms = itertools.permutations([0, 1, 2])
# for i in perms:
#     if not isinstance(i, tuple):
#         assert 'Element is not a tuple'
#     print(i)

for i in perms:
    print(list(itertools.dropwhile(lambda x: x <= 0, i)))

