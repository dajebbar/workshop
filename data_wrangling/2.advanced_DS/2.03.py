def stack_push(s, val):
    return s + [val]

def stack_pop(s):
    tos = s[-1]
    del s[-1]
    return tos

url_stack = []

# s = ['a', 'm', 'e', 'n', 'd', 'i', 'n', 'e']
# print(stack_pop(s))