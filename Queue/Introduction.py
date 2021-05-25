##USING LIST
"""
queue = []
def enqueue():
    ele = int(input("Enter the Element: "))
    queue.append(ele)
    print("Elements added are: ", queue)

def dequeue():
    if not queue:
        print("The Queue is empty. ")
    else:
        e = queue.pop(0)
        print("Removed element: ", e)

def display():
    print(queue)

while True:
    print("Enter the choices:"
          " 1. Add "
          " 2. Remove "
          " 3. Show "
          " 4. Quit ")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Choice the correct option. ")
"""

##USING DOUBLE ENDED QUEUE (collections.deque)
"""
from collections import deque

q = deque()

print(q)
#Appending the elements
q.append(10)    #--> 1st value entered
q.append(20)    #--> 2st value entered
q.append(30)    #--> 3st value entered
print("Elements added:", q)
# Elements added: deque([10, 20, 30])

#Removing elements
e = q.popleft()
print("Removed:", e)    #--> 1st value removed is 10.
e = q.popleft()
print("Removed:", e)    #--> 2nd value removed is 20.
# Removed: 10 then Removed: 20

# print("\n")
##Another Way
#Appending elements
q.appendleft(40)    #--> 1st element inserted
q.appendleft(50)    #--> 2st element inserted
q.appendleft(60)    #--> 3st element inserted
print("Added elements:", q)
# Added elements: deque([60, 50, 40])

#Removing elements
e = q.pop()
print("Removed:", e)    #1st element to be removed is 40.
# Removed: 40
"""

##USING queue (queue.Oueue)
# Python program to
# demonstrate implementation of
# queue using queue module


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())






