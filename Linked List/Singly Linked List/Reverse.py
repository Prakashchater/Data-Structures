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

    #Reverse a Linked list

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive_(curr, prev):
            if not curr:
                return prev

            nxt = curr.ref
            curr.ref = prev
            prev = curr
            curr = nxt
            return _reverse_recursive_(curr, prev)
        self.head = _reverse_recursive_(curr=self.head, prev=None)





LL1 = SinglyLL()
LL1.addBegin(20)
LL1.addBegin(10)
LL1.addBegin(0)
# LL1.after_node(200, 10)
# LL1.before_node(100, 10)
LL1.add_end(30)
LL1.add_end(40)
LL1.add_end(50)
# LL1.reverse_iterative()
LL1.reverse_recursive()
LL1.printLL()


