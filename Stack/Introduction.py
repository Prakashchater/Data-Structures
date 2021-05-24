# USING LIST
#Time Complexity: Push - O(N)   Pop - O(N)
"""
n = int(input("Enter the no of elements: "))
stack = []
def push():
    if len(stack) == n:
        print("Stack is full.")
    else:
        ele = int(input("Enter the elements: "))
        stack.append(ele)
        print(stack)

def pop():
    if not stack:
        print("Stack is Empty.")
    else:
        e = stack.pop()
        print("Removed stack", e)
        print(stack)

while True:
    choice = int(input("Enter the choices"
                       " 1. Push"
                       " 2. Pop"
                       " 3. Quit"
                       "\n")
                 )
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter correct choices.")
"""

##IMPLEMENTATION USING COLLECTION DEQUE
#Time Complexity:
# Push: O(1)
# Pop: O(1)
"""
from collections import deque
stack = deque()
n = int(input("Enter the no of elements present in the stack: "))
def push():
    if len(stack) == n:
        print("Stack is Full.")
    else:
        ele = int(input("Enter the Elements: "))
        stack.append(ele)
        print(stack)

def remove():
    if not stack:
        print("Empty Stack")
    else:
        e = stack.pop()
        print("Removed Stack", e)
        print(stack)

while True:
    choice = int(input("Enter the choices"
                       " 1. Push"
                       " 2. Pop"
                       " 3. Quit"
                       "\n")
                 )
    if choice == 1:
        push()
    elif choice == 2:
        remove()
    elif choice == 3:
        break
    else:
        print("Enter correct choices.")
"""
##IMPLEMENTATION USING QUEUE AS LIFO_QUEUE
from queue import LifoQueue
stack = LifoQueue()
# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())


