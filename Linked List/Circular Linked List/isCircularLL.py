class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    ##Traversal method

    def printLL(self):
        if self.head is None:
            print("Linked List is Empty.!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->", end=" ")
                n = n.ref

    ##ADD IN BEGINNING

    def addBegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

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

    def is_circular_list(self, inp_list):
        curr = inp_list.head
        while curr.next:
            curr = curr.next
            if curr.next == inp_list.head:
                return True
        return False


if __name__ == '__main__':
    cLL = CircularLL()
    cLL.append(1)
    cLL.append(2)
    cLL.append(3)
    cLL.append(4)
    cLL.append(5)

    LL = SinglyLL()
    LL.addBegin(5)
    LL.addBegin(4)
    LL.addBegin(3)
    LL.addBegin(2)
    LL.addBegin(1)

    print(cLL.is_circular_list(LL))
    print(cLL.is_circular_list(cLL))

