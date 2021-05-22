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


    def sortedIntersect(self, head1, head2):
        ptr1 = head1
        ptr2 = head2
        head = None
        curr = None
        while ptr1 and ptr2:
            if ptr1.data == ptr2.data:
                if head is None:
                    new_node = Node(ptr1.data)
                    head = new_node
                    curr = new_node
                else:
                    new_node = Node(ptr1.data)
                    curr.ref = new_node
                    curr = curr.ref

                ptr1 = ptr1.ref
                ptr2 = ptr2.ref

            else:
                if ptr1.data < ptr2.data:
                    ptr1 = ptr1.ref

                else:
                    ptr2 = ptr2.ref

        return head





if __name__ == '__main__':
    LL1 = SinglyLL()
    LL2 = SinglyLL()

    LL1.addBegin(2)
    LL1.addBegin(4)
    LL1.addBegin(6)
    LL1.addBegin(8)
    LL1.addBegin(10)
    LL1.printLL()
    print("\n")

    LL2.addBegin(2)
    LL2.addBegin(4)
    # LL2.addBegin(6)
    LL2.printLL()
    print("\n")

    res = SinglyLL()
    res.head = res.sortedIntersect(LL1.head, LL2.head)
    res.printLL()

