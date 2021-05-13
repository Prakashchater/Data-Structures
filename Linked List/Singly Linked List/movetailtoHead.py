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
                print(n.data, "-->", end=" ")
                n = n.ref

    def addToList(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref:
            n = n.ref
        n.ref = new_node

    def moveTailToHead(self):
        last_node = self.head
        second_last_node = None
        while last_node.ref is not None:
            second_last_node = last_node
            last_node = last_node.ref
        last_node.ref = self.head
        second_last_node.ref = None
        self.head = last_node

if __name__ == '__main__':
    LL1 = SinglyLL()
    LL1.addToList("A")
    LL1.addToList("B")
    LL1.addToList("C")
    LL1.addToList("D")
    LL1.addToList("E")
    LL1.moveTailToHead()
    LL1.printLL()