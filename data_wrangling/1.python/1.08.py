import random


list_1 = [random.randint(0, 30) for _ in range (0, 100)]

# Create a unique valued list from list_1
print(list_1, end=' ')
print()
print(list(dict.fromkeys(list_1).keys())[:10], end=' ')