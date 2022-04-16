from collections import deque

my_queue = deque([])
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

my_queue.popleft()
print(my_queue)

if not my_queue:
    print ("empty queue")