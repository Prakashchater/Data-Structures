# Time: O(N)
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

    def removeDuplicate(self, head):
        if head is None:
            return None

        s = set()
        curr = head
        s.add(self.head.ref)

        while curr.ref is not None:
            if curr.ref.data in s:
                curr.ref = curr.ref.ref
            else:
                s.add(curr.ref.data)
                curr = curr.ref
        return head

if __name__ == '__main__':

    LL1 = SinglyLL()
    LL1.addBegin(4)
    LL1.addBegin(2)
    LL1.addBegin(1)
    LL1.addBegin(4)
    LL1.addBegin(1)
    LL1.addBegin(3)
    LL1.addBegin(2)
    LL1.printLL()
    print("\n")
    LL1.head = LL1.removeDuplicate(LL1.head)
    LL1.printLL()


