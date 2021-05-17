class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            curr = self.head
            new_node = Node(data)
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def printCLL(self):
        curr = self.head
        while curr is not None:
            print(curr.data, "-->", end=" ")
            curr = curr.next
            if curr == self.head:
                break

if __name__ == '__main__':
    cLL = CircularLL()
    cLL.prepend("B")
    cLL.prepend("A")
    cLL.append("C")
    cLL.append("D")
    cLL.printCLL()