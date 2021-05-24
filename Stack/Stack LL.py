class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    ##CHECK IF STACK IS EMPTY
    def is_empty(self):
        return self.size == 0

    ##PRINTING STACK
    def __str__(self):
        curr = self.head.next
        out = ""
        while curr:
            out += str(curr.data) + " --> "
            curr = curr.next
        return out[:-3]

    ##GETTING THE CURRENT SIZE
    def getSize(self):
        return self.size

    ##RETURN TOP ELEMENT IN THE STACK
    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack.")
        return self.head.next.data

    ##APPENDING THE ELEMENT IN THE STACK
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1


    def pop(self):
        if self.is_empty():
            raise Exception("Popping element from an empty stack.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data

if __name__ == '__main__':
    s = Stack()
    for i in range(1, 11):
        s.push(i)
    print(f"Stack: {s}")

    for i in range(1, 6):
        remove = s.pop()
        print(f"Removed: {remove}")
    print(f"Stack: {s}")




