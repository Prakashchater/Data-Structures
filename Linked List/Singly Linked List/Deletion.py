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

    ##DELETE IN BEGIN

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty you cannot delete...!")
        else:
            self.head = self.head.ref

    ##DELETE AT THE END
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty you cannot delete.!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    ##DELETE BY VALUE
    def delete_by_value(self, x):
        if self.head is None:
            print("Cant delete Linked list is empty.!")
            return
        # If the given node is first node
        if x == self.head.data:
            self.head = self.head.ref
            return
        #If the linked list is by value
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        #If the value is not present
        if n.ref is None:
            print("Node is not present.")
        else:
            n.ref = n.ref.ref



LL1 = SinglyLL()
LL1.addBegin(20)
LL1.addBegin(10)
LL1.add_end(30)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(20)
LL1.printLL()


