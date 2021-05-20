class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


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

    ##AT THE END
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def deleteLoop(self, node):
        ptr1 = self.head
        while True:
            ptr2 = node
            while ptr2.ref != node and ptr2.ref != ptr1:
                ptr2 = ptr2.ref

            if ptr2.ref == ptr1:
                break

            ptr1 = ptr1.ref

        ptr2.ref = None


    def deleteAndDetectLoop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.ref is not None:
            slow = slow.ref
            fast = fast.ref.ref

            if slow == fast:
                self.deleteLoop(slow)
                return 1
        return 0

if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addBegin(5)
    LL1.addBegin(4)
    LL1.addBegin(3)
    LL1.addBegin(2)
    LL1.addBegin(1)
    LL1.head.ref.ref.ref.ref.ref = LL1.head.ref.ref
    LL1.deleteAndDetectLoop()
    print("Linked List after removing loop")
    LL1.printLL()
