class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def printCLL(self):
        if self.head is None:
            print("Circular Linked list is empty.")
        else:
            curr = self.head
            while curr:
                print(curr.data, "-->", end=" ")
                curr = curr.next
                if curr == self.head:
                    break

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

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def deletion_node(self, node):
        #IF IT IS A HEAD NODE
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next

    def josephusCircle(self, step):
        curr = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            print("REMOVED :" + str(curr.data))
            self.deletion_node(curr)
            curr = curr.next


if __name__ == '__main__':
    cLL = CircularLL()
    cLL.append("C")
    cLL.append("D")
    cLL.prepend("B")
    cLL.prepend("A")
    cLL.josephusCircle(2)
    cLL.printCLL()

