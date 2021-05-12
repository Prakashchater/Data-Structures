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


    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()
        if self.head is None or self.head.ref is None:
            return self.head

        while curr is not None:
            if curr.data in dup_values:
                #remove nodes
                prev.ref = curr.ref
                curr = None
            else:
                #when we encounter no duplicate values
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.ref

LL1 = SinglyLL()
LL1.addToList(1)
# LL1.addToList(6)
# LL1.addToList(1)
# LL1.addToList(4)
# LL1.addToList(2)
# LL1.addToList(2)
# LL1.addToList(4)
LL1.remove_duplicates()
LL1.printLL()
