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


    def removeDuplicate(self):
        if self.head is None:
            return None

        curr = self.head
        while curr.ref is not None:
            if curr.data == curr.ref.data:
                curr.ref = curr.ref.ref
            else:
                curr = curr.ref

        return curr

if __name__ == '__main__':

    LL1 = SinglyLL()
    LL1.addBegin(2)
    LL1.addBegin(3)
    LL1.addBegin(3)
    LL1.addBegin(4)
    LL1.addBegin(5)
    LL1.addBegin(5)
    LL1.removeDuplicate()
    LL1.printLL()

