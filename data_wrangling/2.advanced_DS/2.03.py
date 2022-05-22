def stack_push(s, val):
    return s + [val]

def stack_pop(s):
    tos = s[-1]
    del s[-1]
    return tos

url_stack = []

# s = ['a', 'm', 'e', 'n', 'd', 'i', 'n', 'e']
# print(stack_pop(s))

wikipedia_datascience = """Data science is an interdisciplinary
field that uses scientific methods, processes, algorithms and systems
to extract knowledge [https://en.wikipedia.org/wiki/Knowledge] and
insights from data [https://en.wikipedia.org/wiki/Data] in various
forms, both structured and unstructured,similar to data mining
[https://en.wikipedia.org/wiki/Data_mining]"""

# print(f'the length: {len(wikipedia_datascience)}')

wd_lst = wikipedia_datascience.split()
# print(wd_lst)

# print(f'length of list: {len(wd_lst)}')

for word in wd_lst:
    if word.startswith('[http'):
        url_stack = stack_push(url_stack, word[1:-1])
        print(word[-1:1])

print(url_stack)