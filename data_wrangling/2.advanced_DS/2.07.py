import time
from collections import deque


# Implementing a queue
print("---Queue as list---")
queue = []
start = time.time()
for item in range(0, 100000):
    queue.append(item)
end = time.time()
print("Queue created")
# print(queue)
print(end-start)

start = time.time()
for _ in range(0, 100000):
    queue.pop(0)
end = time.time()
print(end-start)
print('queue 1 empted')

print("---Queue as deque---")
d = deque()
start = time.time()
for item in range(0, 100000):
    d.append(item)
end = time.time()
print("Queue created")
# print(d)
print(end-start)

start = time.time()
for _ in range(0, 100000):
    d.popleft()
end = time.time()
print(end-start)
print('queue 2 empted')

