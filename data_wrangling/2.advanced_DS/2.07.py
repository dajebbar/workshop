import time


# Implementing a queue

queue = []
start = time.time()
for item in range(0, 100000):
    queue.append(item)
end = time.time()
print("Queue created")
print(queue)
print(end-start)