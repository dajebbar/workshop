import itertools

perms = itertools.permutations([0, 1, 2])
# for i in perms:
#     if not isinstance(i, tuple):
#         assert 'Element is not a tuple'
#     print(i)

# for i in perms:
#     print(list(itertools.dropwhile(lambda x: x <= 0, i)))


def get_content_numbers(stack_lst):
    num_gen = 0
    for i in range(len(stack_lst)):
        num_gen += stack_lst.pop() * 10**i
    return float(num_gen)

for i in perms:
    stack_lst = list(itertools.dropwhile(lambda x: x <= 0, i))
    print(get_content_numbers(stack_lst))