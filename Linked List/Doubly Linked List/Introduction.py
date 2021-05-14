class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    ##FORWARD TRAVERSAL
    def forward_printLL(self):
        if self.head is None:
            print("Linked list is empty!.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    ##BACKWARD TRAVERSAL
    def backward_printLL(self):
        if self.head is None:
            print("Linked list is empty.!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

dLL = DoublyLL()
dLL.forward_printLL()
dLL.backward_printLL()