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

    ##ADD AFTER A NODE
    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    ##ADD BEFORE NODE
    def before_node(self, data, x):
        if self.head is None:
            print("Linked list is Empty!.")
            return
        if x == self.head.data:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present in the Linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


    def kth_reverse(self, head, k):
        if head is None:
            return None
        curr = head
        next = None
        prev = None
        count = 0

        while curr is not None and count < k:
            next = curr.ref
            curr.ref = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.ref = self.kth_reverse(next, k)
        return prev


LL1 = SinglyLL()
LL1.addBegin(9)
LL1.addBegin(8)
LL1.addBegin(7)
LL1.addBegin(6)
LL1.addBegin(5)
LL1.addBegin(4)
LL1.addBegin(3)
LL1.addBegin(2)
LL1.addBegin(1)
LL1.head = LL1.kth_reverse(LL1.head, 4)
LL1.printLL()


