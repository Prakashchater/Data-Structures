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

    ##INSERT WHEN EMPTY
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")

    ##INSERT AT THE BEGINNING
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    ##INSERT AT THE END
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    ##ADD AFTER GIVEN NODE
    def add_after(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node is not found in DLL.")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    ##INSERT BEFORE A GIVEN NODE
    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Node not found in DLL.")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node



if __name__ == '__main__':
    dLL = DoublyLL()
    dLL.add_begin(10)
    dLL.add_begin(20)
    dLL.add_end(30)
    dLL.add_after(40, 30)
    dLL.add_before(50, 10)
    dLL.add_before(60, 20)
    dLL.forward_printLL()
    # print("\n")
    # dLL.backward_printLL()

